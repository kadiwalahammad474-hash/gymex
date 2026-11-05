/* ================================================================
   POST /api/demo-lead
   Demo form ka server-side submit.

   - Captcha server par verify hota hai (HMAC token + expiry).
   - Sender ka IP server headers se nikalta hai (browser se nahi).
   - Lead SendGrid se support@gymex.online par jaati hai (sales CC).
   - Per-IP rate limit, honeypot aur basic validation.

   Required env var: SENDGRID_API_KEY
   Optional: SENDGRID_FROM, SENDGRID_TO, SENDGRID_CC, CAPTCHA_SECRET
   ================================================================ */

const crypto = require('crypto');

const SECRET = process.env.CAPTCHA_SECRET || 'gymex-demo-captcha-v1';
const TTL_MS = 5 * 60 * 1000;
const RATE_WINDOW_MS = 10 * 60 * 1000;
const RATE_MAX = 4;

const hits = global.__gymexLeadHits || (global.__gymexLeadHits = new Map());

function sign(ts, answer) {
  return crypto
    .createHmac('sha256', SECRET)
    .update(ts + ':' + answer)
    .digest('hex')
    .slice(0, 32);
}

function checkCaptcha(token, input) {
  if (!token || !input) return 'missing';
  const parts = String(token).split('.');
  if (parts.length !== 2) return 'bad_token';
  const ts = parseInt(parts[0], 10);
  if (!ts || Number.isNaN(ts)) return 'bad_token';
  if (Date.now() - ts > TTL_MS) return 'expired';
  const expected = sign(ts, String(input).trim().toUpperCase());
  const given = String(parts[1]);
  if (expected.length !== given.length) return 'wrong';
  if (!crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(given))) return 'wrong';
  return null;
}

function clientIp(headers) {
  const fwd = headers['x-forwarded-for'] || headers['X-Forwarded-For'];
  if (fwd) {
    const first = String(fwd).split(',')[0].trim();
    if (first) return first;
  }
  return (
    headers['x-real-ip'] ||
    headers['cf-connecting-ip'] ||
    headers['x-vercel-forwarded-for'] ||
    'unknown'
  );
}

function clean(value, max) {
  return String(value == null ? '' : value).trim().slice(0, max || 500);
}

function escapeHtml(value) {
  return clean(value, 4000)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function buildHtml(data) {
  const rows = [
    ['Name', data.firstname + ' ' + data.lastname],
    ['Company / Gym', data.company || '-'],
    ['Email', data.email],
    ['Phone', data.phonenumber || '-'],
    ['Message', data.message || '-'],
    ['IP Address', data.ip],
    ['Country', data.country || '-'],
    ['Page', data.page || '-'],
    ['Browser', data.userAgent],
    ['Received', data.receivedAt],
  ];

  const body = rows
    .map((row, i) => {
      const bg = i % 2 === 0 ? 'background:#f7f9fc;' : '';
      return (
        '<tr style="' + bg + '">' +
        '<td style="padding:8px;font-weight:bold;width:34%;border:1px solid #e0e6f0;color:#1b2b4b;">' +
        escapeHtml(row[0]) + '</td>' +
        '<td style="padding:8px;border:1px solid #e0e6f0;color:#4a5568;line-height:18px;">' +
        escapeHtml(row[1]) + '</td></tr>'
      );
    })
    .join('');

  return (
    '<div style="max-width:560px;margin:auto;font-family:Arial,sans-serif;background:#fff;' +
    'border:1px solid #e5e8ef;border-radius:10px;overflow:hidden;">' +
    '<div style="background:#0b1a3d;padding:14px;text-align:center;">' +
    '<h3 style="color:#fff;margin:0;font-size:15px;font-weight:700;letter-spacing:.4px;">' +
    'New Website Demo Request</h3></div>' +
    '<div style="padding:16px;">' +
    '<p style="font-size:13px;color:#555;margin:0 0 12px;line-height:19px;">' +
    'One new demo request came from the website. Details below:</p>' +
    '<table style="width:100%;border-collapse:collapse;font-size:12.5px;">' + body + '</table>' +
    '</div>' +
    '<div style="background:#f5f7fa;padding:10px;text-align:center;font-size:11px;color:#8892a5;' +
    'border-top:1px solid #e0e6f0;">Sent from the Gymex website demo form.</div></div>'
  );
}

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');

  if (req.method !== 'POST') {
    res.status(405).json({ ok: false, error: 'method_not_allowed' });
    return;
  }

  let body = req.body;
  if (typeof body === 'string') {
    try {
      body = JSON.parse(body);
    } catch (e) {
      body = null;
    }
  }
  if (!body || typeof body !== 'object') {
    res.status(400).json({ ok: false, error: 'bad_request' });
    return;
  }

  // Honeypot — bots isko bhar dete hain, humans nahi dekhte.
  if (clean(body.website)) {
    res.status(200).json({ ok: true });
    return;
  }

  const email = clean(body.email, 120);
  const firstname = clean(body.firstname, 80);
  const lastname = clean(body.lastname, 80);
  const company = clean(body.company, 120);
  const phonenumber = clean(body.phonenumber, 30);
  const message = clean(body.message, 2000);
  const page = clean(body.page, 300);

  if (!firstname || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) {
    res.status(400).json({ ok: false, error: 'invalid_fields' });
    return;
  }

  const headers = req.headers || {};
  const ip = clientIp(headers);

  const captchaError = checkCaptcha(body.captchaToken, body.captcha);
  if (captchaError) {
    res.status(400).json({ ok: false, error: 'captcha_' + captchaError });
    return;
  }

  // Simple per-IP rate limit (best effort, per warm instance).
  const now = Date.now();
  const record = hits.get(ip) || [];
  const recent = record.filter((t) => now - t < RATE_WINDOW_MS);
  if (recent.length >= RATE_MAX) {
    res.status(429).json({ ok: false, error: 'too_many_requests' });
    return;
  }
  recent.push(now);
  hits.set(ip, recent);

  const apiKey = process.env.SENDGRID_API_KEY;
  if (!apiKey) {
    res.status(503).json({ ok: false, error: 'email_not_configured' });
    return;
  }

  const payload = {
    personalizations: [
      {
        to: [{ email: process.env.SENDGRID_TO || 'support@gymex.online' }],
        cc: [{ email: process.env.SENDGRID_CC || 'sales@gymex.online' }],
        subject: 'New Demo Request From Website',
      },
    ],
    from: {
      email: process.env.SENDGRID_FROM || 'noreply@gymex.online',
      name: 'Gymex Website',
    },
    reply_to: { email: email },
    content: [
      {
        type: 'text/html',
        value: buildHtml({
          firstname,
          lastname,
          company,
          email,
          phonenumber,
          message,
          ip,
          country: headers['x-vercel-ip-country'] || '',
          page,
          userAgent: clean(headers['user-agent'], 200),
          receivedAt: new Date().toISOString(),
        }),
      },
    ],
  };

  try {
    const response = await fetch('https://api.sendgrid.com/v3/mail/send', {
      method: 'POST',
      headers: {
        Authorization: 'Bearer ' + apiKey,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (response.status >= 200 && response.status < 300) {
      res.status(200).json({ ok: true });
      return;
    }

    const detail = await response.text();
    console.error('SendGrid error', response.status, detail.slice(0, 300));
    res.status(502).json({ ok: false, error: 'send_failed' });
  } catch (err) {
    console.error('SendGrid request failed', err && err.message);
    res.status(502).json({ ok: false, error: 'send_failed' });
  }
};

module.exports._checkCaptcha = checkCaptcha;
module.exports._clientIp = clientIp;
