/* ================================================================
   GYMEX demo form — server-side submit (js/demo-form.js)

   Har page ka "GET YOUR FREE DEMO" popup isi se chalta hai:

   1. Form me server-captcha (SVG + HMAC token) inject karta hai.
   2. Submit ko capture phase me rok kar khud /api/demo-lead par
      bhejta hai — IP server par headers se liya jaata hai.
   3. Success par page ka hi thank-you block dikhata hai.
   4. Email service configure na ho to saaf error dikhata hai
      (silently fail nahi karta).

   javascript.js ise har page par load karti hai.
   ================================================================ */
(function () {
  'use strict';

  var state = { token: '', loading: false, form: null };
  var CAPTCHA_ENDPOINT = '/api/captcha';
  var LEAD_ENDPOINT = '/api/demo-lead';

  var ERROR_TEXT = {
    captcha_missing: 'Please enter the security code.',
    captcha_wrong: 'Security code is incorrect. Please try the new code.',
    captcha_expired: 'Security code expired. Please enter the new code.',
    captcha_bad_token: 'Security code expired. Please enter the new code.',
    invalid_fields: 'Please fill your name and a valid email address.',
    too_many_requests: 'Too many requests. Please try again in a few minutes.',
    email_not_configured: 'Form is not connected to email yet. Please email support@gymex.online.',
    send_failed: 'Could not send right now. Please try again or email support@gymex.online.',
    network: 'Network error. Please check your connection and try again.'
  };

  function $(sel, root) {
    return (root || document).querySelector(sel);
  }

  function buildCaptchaBox() {
    var box = document.createElement('div');
    box.className = 'gx-captcha';
    box.style.cssText =
      'display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-top:14px;' +
      "font-family:'Poppins',sans-serif;";
    box.innerHTML =
      '<div style="display:flex;align-items:center;gap:8px;">' +
      '<img class="gx-captcha-img" alt="Security code" width="210" height="66" style="height:56px;width:auto;' +
      'border:1.5px solid #e0e6f0;border-radius:8px;background:#f4f7fb;display:block;cursor:pointer;">' +
      '<button type="button" class="gx-captcha-refresh" title="New code" ' +
      'style="background:#fff;border:1.5px solid #e0e6f0;border-radius:8px;color:#1565C0;' +
      'font-size:15px;padding:8px 11px;cursor:pointer;line-height:1;">&#8635;</button>' +
      '</div>' +
      '<input type="text" class="gx-captcha-input" placeholder="Enter the code" maxlength="6" ' +
      'autocomplete="off" spellcheck="false" ' +
      "style=\"padding:11px 12px;border:1.5px solid #e0e6f0;border-radius:8px;font-size:13px;width:150px;" +
      "font-family:'Poppins',sans-serif;color:#333;outline:none;text-transform:uppercase;\">" +
      '<p class="gx-captcha-msg" style="flex:1 0 100%;margin:0;font-size:12.5px;color:#e0450b;' +
      'display:none;font-weight:600;"></p>';
    return box;
  }

  function showMessage(text, isError) {
    if (!state.form) return;
    var msg = $('.gx-captcha-msg', state.form);
    if (!msg) return;
    if (!text) {
      msg.style.display = 'none';
      msg.textContent = '';
      return;
    }
    msg.textContent = text;
    msg.style.color = isError ? '#e0450b' : '#1a7f37';
    msg.style.display = 'block';
  }

  function loadCaptcha() {
    if (!state.form) return;
    var img = $('.gx-captcha-img', state.form);
    var input = $('.gx-captcha-input', state.form);
    if (input) input.value = '';
    state.token = '';
    if (img) img.style.opacity = '0.5';
    state.loading = true;

    fetch(CAPTCHA_ENDPOINT + '?t=' + Date.now(), { cache: 'no-store' })
      .then(function (r) {
        if (!r.ok) throw new Error('captcha ' + r.status);
        return r.json();
      })
      .then(function (data) {
        state.token = data.token || '';
        if (img && data.image) img.src = data.image;
        if (img) img.style.opacity = '1';
        state.loading = false;
      })
      .catch(function () {
        state.loading = false;
        if (img) img.style.opacity = '1';
        showMessage('Security code load nahi hua. Refresh karke try karein.', true);
      });
  }

  function valueOf(form, id, name) {
    var el = form.querySelector('#' + id) || (name ? form.querySelector('[name="' + name + '"]') : null);
    return el ? el.value : '';
  }

  function setBusy(busy) {
    var btn = state.form && state.form.querySelector('button[type="submit"]');
    if (!btn) return;
    if (busy) {
      btn.dataset.gxLabel = btn.dataset.gxLabel || btn.textContent;
      btn.disabled = true;
      btn.textContent = 'Sending...';
    } else {
      btn.disabled = false;
      if (btn.dataset.gxLabel) btn.textContent = btn.dataset.gxLabel;
    }
  }

  function showSuccess() {
    var body = document.getElementById('form-body');
    var success = document.getElementById('emailsuccessmsg');
    if (body) body.style.display = 'none';
    if (success) success.style.display = 'block';
    var modal = $('.contact-us');
    if (modal && modal.scrollTo) modal.scrollTo({ top: 0, behavior: 'smooth' });
    if (state.form) state.form.reset();
    loadCaptcha();
  }

  function submitLead(form) {
    var code = ($('.gx-captcha-input', form) || {}).value || '';
    code = code.trim();

    if (!state.token) {
      showMessage('Security code load ho raha hai, ek second ruk jayein.', true);
      loadCaptcha();
      return;
    }
    if (!code) {
      showMessage(ERROR_TEXT.captcha_missing, true);
      return;
    }

    var payload = {
      firstname: valueOf(form, 'first-name', 'firstname'),
      lastname: valueOf(form, 'last-name', 'lastname'),
      company: valueOf(form, 'company', 'company'),
      email: valueOf(form, 'email', 'email'),
      phonenumber: valueOf(form, 'number', 'phonenumber'),
      message: valueOf(form, 'message', 'message') || (form.message ? form.message.value : ''),
      captcha: code.toUpperCase(),
      captchaToken: state.token,
      page: window.location.href,
      website: valueOf(form, 'gx-website', 'website'),
    };

    showMessage('');
    setBusy(true);

    fetch(LEAD_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    })
      .then(function (r) {
        return r.json().then(function (data) {
          return { ok: r.ok, data: data };
        });
      })
      .then(function (res) {
        setBusy(false);
        if (res.ok && res.data && res.data.ok) {
          showSuccess();
          return;
        }
        var err = (res.data && res.data.error) || 'send_failed';
        showMessage(ERROR_TEXT[err] || ERROR_TEXT.send_failed, true);
        loadCaptcha();
      })
      .catch(function () {
        setBusy(false);
        showMessage(ERROR_TEXT.network, true);
        loadCaptcha();
      });
  }

  function setupForm() {
    var form = document.getElementById('contact-form');
    if (!form || form.dataset.gxReady === '1') return;
    form.dataset.gxReady = '1';
    state.form = form;

    var box = buildCaptchaBox();
    var honeypot = document.createElement('input');
    honeypot.type = 'text';
    honeypot.name = 'website';
    honeypot.id = 'gx-website';
    honeypot.tabIndex = -1;
    honeypot.autocomplete = 'off';
    honeypot.style.cssText = 'position:absolute;left:-9999px;width:1px;height:1px;opacity:0;';
    box.appendChild(honeypot);

    var submitBtn = form.querySelector('button[type="submit"]');
    if (submitBtn) {
      form.insertBefore(box, submitBtn);
    } else {
      form.appendChild(box);
    }

    form.addEventListener('click', function (e) {
      if (e.target.closest && e.target.closest('.gx-captcha-refresh, .gx-captcha-img')) {
        e.preventDefault();
        loadCaptcha();
      }
    });

    loadCaptcha();
  }

  // Submit ko capture phase me hi rok lete hain, taake page ke purane
  // EmailJS handlers (jo ab kaam nahi karte) chal hi na sakein.
  document.addEventListener(
    'submit',
    function (e) {
      var form = e.target;
      if (!form || form.id !== 'contact-form') return;
      e.preventDefault();
      e.stopPropagation();
      submitLead(form);
    },
    true
  );

  function refreshOnOpen() {
    var openers = document.querySelectorAll(
      '.open-modal-btn, #demobutton, [data-open-modal]'
    );
    Array.prototype.forEach.call(openers, function (btn) {
      btn.addEventListener('click', function () {
        setTimeout(function () {
          if (!state.form) setupForm();
          if (state.form && !state.token) loadCaptcha();
        }, 250);
      });
    });
  }

  function init() {
    setupForm();
    refreshOnOpen();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
