/* ================================================================
   GYMEX — reCAPTCHA reliability guard (js/captcha-guard.js)

   Har demo/contact form Google reCAPTCHA v2 (checkbox) use karta hai.
   Kuch pages mein #recaptcha-error element missing tha, jiski wajah se
   submit handler `null.style` par crash ho jata tha aur form submit hi
   nahi hota tha. Ye file sab pages par load hoti hai aur:

     1. #recaptcha-error element inject karti hai (agar na ho).
     2. onRecaptchaSuccess / onRecaptchaExpired ko safe banati hai
        (missing element par bhi throw na kare).
     3. Demo modal khulne par purana token reset karti hai.
     4. Google ka widget load na ho (network/adblock) to friendly
        retry message dikhati hai, silently fail nahi karti.
     5. Empty response par user ko widget tak scroll karti hai.
   ================================================================ */
(function () {
  'use strict';

  var ERROR_ID = 'recaptcha-error';
  var ERROR_TEXT = 'Please verify that you are not a robot.';
  var LOAD_FAIL_TEXT = 'Captcha load nahi hua. Internet check karke retry karein.';

  function widgetEls() {
    return Array.prototype.slice.call(document.querySelectorAll('.g-recaptcha'));
  }

  function ensureErrorEl() {
    if (document.getElementById(ERROR_ID)) return document.getElementById(ERROR_ID);
    var widget = widgetEls()[0];
    var p = document.createElement('p');
    p.id = ERROR_ID;
    p.style.cssText = 'display:none;text-align:center;color:#ef4444;font-size:12.5px;' +
      "font-family:'Poppins',sans-serif;margin:8px auto 0;line-height:1.5;";
    p.textContent = ERROR_TEXT;
    if (widget && widget.parentNode) {
      widget.parentNode.insertBefore(p, widget.nextSibling);
    } else {
      (document.querySelector('.form-wrap') || document.body).appendChild(p);
    }
    return p;
  }

  function showError(msg) {
    var el = ensureErrorEl();
    if (!el) return;
    if (msg) el.textContent = msg;
    el.style.display = 'block';
  }

  function hideError() {
    var el = document.getElementById(ERROR_ID);
    if (el) el.style.display = 'none';
  }

  // Google inhi globals ko naam se call karta hai (data-callback).
  // Page apna version define karta hai; use crash-proof wrapper me daal dete hain.
  function wrapGlobal(name, after) {
    var original = window[name];
    window[name] = function () {
      try {
        if (typeof original === 'function') original.apply(this, arguments);
      } catch (e) {
        /* element missing tha — ignore, form ab bhi kaam karega */
      }
      try {
        after && after();
      } catch (e) {}
    };
  }

  function resetWidget() {
    try {
      if (window.grecaptcha && typeof window.grecaptcha.reset === 'function') {
        window.grecaptcha.reset();
      }
    } catch (e) {}
  }

  // Google script load na ho to user ko pata chale + retry mile.
  function watchLoad() {
    var widget = widgetEls()[0];
    if (!widget) return;

    setTimeout(function () {
      var rendered = widget.querySelector('iframe') || widget.children.length > 0;
      if (rendered) return;
      var el = ensureErrorEl();
      if (!el) return;
      el.innerHTML = LOAD_FAIL_TEXT.replace(
        'retry karein',
        '<a href="javascript:location.reload()" style="color:#028ece;font-weight:600;text-decoration:underline;">retry</a> karein'
      );
      el.style.display = 'block';
    }, 9000);
  }

  function bindModalResets() {
    // Demo modal khulta hai to purana (expired) token clear kar do.
    var openers = document.querySelectorAll(
      '.open-modal-btn, #demobutton, [data-open-modal], a[href="#demo"], button[data-demo]'
    );
    Array.prototype.forEach.call(openers, function (btn) {
      btn.addEventListener('click', function () {
        hideError();
        setTimeout(resetWidget, 120);
      });
    });
  }

  // Submit par captcha empty ho to user ko widget dikhao (page ka apna error bhi chalta hai).
  function watchSubmit() {
    document.addEventListener(
      'submit',
      function (e) {
        var form = e.target;
        if (!form || !form.querySelector || !form.querySelector('.g-recaptcha')) return;
        var token = '';
        try {
          token = window.grecaptcha && window.grecaptcha.getResponse ? window.grecaptcha.getResponse() : '';
        } catch (err) {}
        if (!token) {
          showError();
          var widget = form.querySelector('.g-recaptcha');
          if (widget && widget.scrollIntoView) {
            widget.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        } else {
          hideError();
        }
      },
      true
    );
  }

  function init() {
    ensureErrorEl();
    wrapGlobal('onRecaptchaSuccess', hideError);
    wrapGlobal('onRecaptchaExpired', hideError);
    bindModalResets();
    watchSubmit();
    watchLoad();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
