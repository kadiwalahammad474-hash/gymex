/* ================================================================
   GET /api/captcha
   Server-side captcha for the demo form.

   - Code ki image ek real PNG hai (SVG text jaisa readable nahi).
   - Distortion: per-character scale, offset, row shear + noise lines.
   - Answer response me nahi jaata: sirf HMAC-signed token
     (timestamp + hashed answer) jaata hai, verification
     /api/demo-lead par hoti hai. Token 5 minute me expire hota hai.
   ================================================================ */

const crypto = require('crypto');
const zlib = require('zlib');

const SECRET = process.env.CAPTCHA_SECRET || 'gymex-demo-captcha-v1';
const TTL_MS = 5 * 60 * 1000;
const LETTERS = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';

/* ---------- tiny 5x7 bitmap font (no dependencies) ---------- */
const FONT = {
  A: ['01110', '10001', '10001', '11111', '10001', '10001', '10001'],
  B: ['11110', '10001', '10001', '11110', '10001', '10001', '11110'],
  C: ['01110', '10001', '10000', '10000', '10000', '10001', '01110'],
  D: ['11110', '10001', '10001', '10001', '10001', '10001', '11110'],
  E: ['11111', '10000', '10000', '11110', '10000', '10000', '11111'],
  F: ['11111', '10000', '10000', '11110', '10000', '10000', '10000'],
  G: ['01110', '10001', '10000', '10111', '10001', '10001', '01111'],
  H: ['10001', '10001', '10001', '11111', '10001', '10001', '10001'],
  J: ['00111', '00010', '00010', '00010', '00010', '10010', '01100'],
  K: ['10001', '10010', '10100', '11000', '10100', '10010', '10001'],
  L: ['10000', '10000', '10000', '10000', '10000', '10000', '11111'],
  M: ['10001', '11011', '10101', '10101', '10001', '10001', '10001'],
  N: ['10001', '11001', '10101', '10011', '10001', '10001', '10001'],
  P: ['11110', '10001', '10001', '11110', '10000', '10000', '10000'],
  Q: ['01110', '10001', '10001', '10001', '10101', '10010', '01101'],
  R: ['11110', '10001', '10001', '11110', '10100', '10010', '10001'],
  S: ['01111', '10000', '10000', '01110', '00001', '00001', '11110'],
  T: ['11111', '00100', '00100', '00100', '00100', '00100', '00100'],
  U: ['10001', '10001', '10001', '10001', '10001', '10001', '01110'],
  V: ['10001', '10001', '10001', '10001', '10001', '01010', '00100'],
  W: ['10001', '10001', '10001', '10101', '10101', '11011', '10001'],
  X: ['10001', '10001', '01010', '00100', '01010', '10001', '10001'],
  Y: ['10001', '10001', '01010', '00100', '00100', '00100', '00100'],
  Z: ['11111', '00001', '00010', '00100', '01000', '10000', '11111'],
  2: ['01110', '10001', '00001', '00010', '00100', '01000', '11111'],
  3: ['11111', '00010', '00100', '00010', '00001', '10001', '01110'],
  4: ['00010', '00110', '01010', '10010', '11111', '00010', '00010'],
  5: ['11111', '10000', '11110', '00001', '00001', '10001', '01110'],
  6: ['00110', '01000', '10000', '11110', '10001', '10001', '01110'],
  7: ['11111', '00001', '00010', '00100', '01000', '01000', '01000'],
  8: ['01110', '10001', '10001', '01110', '10001', '10001', '01110'],
  9: ['01110', '10001', '10001', '01111', '00001', '00010', '01100'],
};

/* ---------- minimal PNG encoder ---------- */
const CRC_TABLE = (() => {
  const table = new Int32Array(256);
  for (let n = 0; n < 256; n++) {
    let c = n;
    for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
    table[n] = c;
  }
  return table;
})();

function crc32(buf) {
  let c = 0xffffffff;
  for (let i = 0; i < buf.length; i++) c = CRC_TABLE[(c ^ buf[i]) & 0xff] ^ (c >>> 8);
  return (c ^ 0xffffffff) >>> 0;
}

function chunk(type, data) {
  const len = Buffer.alloc(4);
  len.writeUInt32BE(data.length, 0);
  const typeBuf = Buffer.from(type, 'ascii');
  const crcBuf = Buffer.alloc(4);
  crcBuf.writeUInt32BE(crc32(Buffer.concat([typeBuf, data])), 0);
  return Buffer.concat([len, typeBuf, data, crcBuf]);
}

function encodePng(width, height, rgb) {
  const raw = Buffer.alloc((width * 3 + 1) * height);
  for (let y = 0; y < height; y++) {
    raw[y * (width * 3 + 1)] = 0;
    rgb.copy(raw, y * (width * 3 + 1) + 1, y * width * 3, (y + 1) * width * 3);
  }
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(width, 0);
  ihdr.writeUInt32BE(height, 4);
  ihdr[8] = 8;
  ihdr[9] = 2;
  ihdr[10] = 0;
  ihdr[11] = 0;
  ihdr[12] = 0;
  return Buffer.concat([
    Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]),
    chunk('IHDR', ihdr),
    chunk('IDAT', zlib.deflateSync(raw, { level: 9 })),
    chunk('IEND', Buffer.alloc(0)),
  ]);
}

function randInt(min, max) {
  return min + crypto.randomInt(0, max - min + 1);
}

function renderPng(text) {
  const W = 210;
  const H = 66;
  const buf = Buffer.alloc(W * H * 3, 0xf4);
  for (let i = 0; i < buf.length; i += 3) {
    buf[i] = 244;
    buf[i + 1] = 247;
    buf[i + 2] = 251;
  }

  const put = (x, y, r, g, b) => {
    if (x < 0 || y < 0 || x >= W || y >= H) return;
    const i = (y * W + x) * 3;
    buf[i] = r;
    buf[i + 1] = g;
    buf[i + 2] = b;
  };

  // noise lines
  for (let n = 0; n < 5; n++) {
    const x1 = randInt(0, W);
    const y1 = randInt(0, H);
    const x2 = randInt(0, W);
    const y2 = randInt(0, H);
    const steps = Math.max(Math.abs(x2 - x1), Math.abs(y2 - y1)) || 1;
    for (let s = 0; s <= steps; s++) {
      const x = Math.round(x1 + ((x2 - x1) * s) / steps);
      const y = Math.round(y1 + ((y2 - y1) * s) / steps);
      put(x, y, 197, 209, 224);
      put(x + 1, y, 210, 220, 232);
    }
  }

  // dots
  for (let n = 0; n < 320; n++) {
    put(randInt(0, W - 1), randInt(0, H - 1), 205, 216, 229);
  }

  const colors = [
    [11, 26, 61],
    [21, 101, 192],
    [2, 142, 206],
    [15, 76, 129],
    [27, 43, 75],
  ];

  const cell = Math.floor((W - 34) / text.length);
  for (let i = 0; i < text.length; i++) {
    const glyph = FONT[text[i]];
    if (!glyph) continue;
    const scale = randInt(3, 4);
    const charW = 5 * scale;
    const charH = 7 * scale;
    const baseX = 18 + i * cell + randInt(0, Math.max(1, cell - charW - 2));
    const baseY = Math.floor((H - charH) / 2) + randInt(-6, 6);
    const shear = (randInt(-16, 16) / 100);
    const color = colors[i % colors.length];

    for (let row = 0; row < 7; row++) {
      const shift = Math.round(row * shear * scale);
      for (let col = 0; col < 5; col++) {
        if (glyph[row][col] !== '1') continue;
        for (let dy = 0; dy < scale; dy++) {
          for (let dx = 0; dx < scale; dx++) {
            put(
              baseX + col * scale + dx + shift,
              baseY + row * scale + dy,
              color[0],
              color[1],
              color[2]
            );
          }
        }
      }
    }
  }

  return encodePng(W, H, buf);
}

function sign(ts, answer) {
  return crypto
    .createHmac('sha256', SECRET)
    .update(ts + ':' + answer)
    .digest('hex')
    .slice(0, 32);
}

module.exports = (req, res) => {
  let answer = '';
  for (let i = 0; i < 6; i++) {
    answer += LETTERS.charAt(crypto.randomInt(0, LETTERS.length));
  }

  const ts = Date.now();
  const token = ts + '.' + sign(ts, answer);
  const png = renderPng(answer);

  res.setHeader('Cache-Control', 'no-store, max-age=0');
  res.setHeader('Content-Type', 'application/json');
  res.status(200).json({
    token: token,
    ttl: TTL_MS,
    image: 'data:image/png;base64,' + png.toString('base64'),
  });
};

module.exports._sign = sign;
module.exports._TTL_MS = TTL_MS;
module.exports._renderPng = renderPng;
