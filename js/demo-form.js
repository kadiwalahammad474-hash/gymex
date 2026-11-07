/* Gymex demo/contact modal form: custom server-verified image captcha + /api/demo-lead submit.
   Replaces brittle inline EmailJS/grecaptcha/hcaptcha handlers site-wide. */
(function () {
  'use strict';
  var CAPTCHA_API = '/api/captcha';
  var LEAD_API = '/api/demo-lead';

  function q(sel, root) { return (root || document).querySelector(sel); }
  function qa(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  function ensureCaptchaUI(form) {
    if (q('.gx-captcha', form)) return q('.gx-captcha', form);
    var host = q('.gx-captcha-host', form) || q('.g-recaptcha', form) || q('.h-captcha', form) || q('#recaptcha-error', form);
    if (!host) return null;
    var wrap = document.createElement('div');
    wrap.className = 'gx-captcha';
    wrap.innerHTML =
      '<div class="gx-captcha-row">' +
        '<div class="gx-captcha-image-wrap">' +
          '<img class="gx-captcha-image" alt="Security code" width="210" height="66">' +
          '<div class="gx-captcha-loading">Loading…</div>' +
        '</div>' +
        '<button type="button" class="gx-captcha-refresh" aria-label="Refresh security code" title="New code">' +
          '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-2.64-6.36"/><polyline points="21 3 21 9 15 9"/></svg>' +
        '</button>' +
      '</div>' +
      '<input type="text" class="contact-us__input gx-captcha-input" name="captcha" autocomplete="off" autocapitalize="characters" spellcheck="false" inputmode="text" maxlength="8" placeholder="Enter security code" required>' +
      '<input type="hidden" name="captchaToken" class="gx-captcha-token">' +
      '<p id="recaptcha-error" class="gx-captcha-error" style="display:none;"></p>';
    host.parentNode.replaceChild(wrap, host);
    qa('#recaptcha-error', form).slice(1).forEach(function (n) { n.parentNode && n.parentNode.removeChild(n); });
    qa('.g-recaptcha,.h-captcha', form).forEach(function (n) { if (!n.classList.contains('gx-captcha')) n.remove(); });
    return wrap;
  }

  function setError(form, msg) {
    var el = q('#recaptcha-error', form) || q('.gx-captcha-error', form);
    if (!el) return;
    el.textContent = msg || '';
    el.style.display = msg ? 'block' : 'none';
  }

  async function loadCaptcha(form, state) {
    if (state.loading) return; state.loading = true;
    var img = q('.gx-captcha-image', form), loading = q('.gx-captcha-loading', form), tokenEl = q('.gx-captcha-token', form), input = q('.gx-captcha-input', form);
    if (!img || !tokenEl) return;
    if (loading) { loading.textContent = 'Loading…'; loading.style.display = 'flex'; }
    setError(form, '');
    try {
      var res = await fetch(CAPTCHA_API + '?t=' + Date.now(), { cache: 'no-store', credentials: 'same-origin' });
      var data = await res.json();
      if (!res.ok || !data || !data.image || !data.token) throw new Error('load');
      img.src = data.image;
      tokenEl.value = data.token;
      state.token = data.token;
      if (input) input.value = '';
      img.onload = function () { if (loading) loading.style.display = 'none'; };
    } catch (e) {
      if (loading) loading.textContent = 'Could not load';
      setError(form, 'Security code could not load. Click refresh or check your connection.');
    }
  }

  function showSuccess(doc) {
    var body = q('#form-body', doc), ok = q('#emailsuccessmsg', doc);
    if (body) body.style.display = 'none';
    if (ok) ok.style.display = 'block';
  }
  function showFail(doc, msg) {
    var eb = q('#emailerrormsg', doc);
    if (eb) { eb.style.display = 'block'; }
    else alert(msg || 'Sorry, submission failed. Please call +91 7710862007 or email sales@gymex.online.');
  }

  function collect(form) {
    var get = function (name) { var el = form.elements[name]; return el ? String(el.value || '').trim() : ''; };
    var phone = q('#number', form);
    var fullPhone = get('phonenumber');
    try { if (phone && window.iti && typeof window.iti.getNumber === 'function') fullPhone = window.iti.getNumber() || fullPhone; } catch (e) {}
    try { if (phone && phone._iti && typeof phone._iti.getNumber === 'function') fullPhone = phone._iti.getNumber() || fullPhone; } catch (e) {}
    return {
      firstname: get('firstname'), lastname: get('lastname'), company: get('company'),
      email: get('email'), phonenumber: fullPhone, message: get('message'),
      captcha: get('captcha'), captchaToken: get('captchaToken'),
      page: window.location.href, website: get('website')
    };
  }

  function bindForm(form) {
    if (!form || form.__gxDemoBound) return;
    if (form.getAttribute('action') && !/^(#|javascript:)/i.test(form.getAttribute('action'))) return;
    form.__gxDemoBound = true;
    // Clone to remove old broken inline handlers (EmailJS/grecaptcha/hcaptcha)
    var clean = form.cloneNode(true);
    form.parentNode.replaceChild(clean, form);
    form = clean;
    // Re-init intl-tel-input if present
    try {
      var phone = q('#number', form);
      if (phone && window.intlTelInput && !phone._iti) {
        window.iti = window.intlTelInput(phone, { utilsScript: 'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js', separateDialCode: true, initialCountry: 'in' });
      }
    } catch (e) {}
    var state = { token: '' };
    var wrap = ensureCaptchaUI(form);
    if (!wrap) return;
    q('.gx-captcha-refresh', form).addEventListener('click', function () { loadCaptcha(form, state); });
    loadCaptcha(form, state);

    window.resetRecaptcha = function () { loadCaptcha(form, state); };
    window.onRecaptchaSuccess = function () { setError(form, ''); };
    window.onRecaptchaExpired = function () { loadCaptcha(form, state); };

    form.addEventListener('submit', async function (e) {
      e.preventDefault();
      e.stopPropagation();
      setError(form, '');
      var eb = q('#emailerrormsg', document); if (eb) eb.style.display = 'none';
      var payload = collect(form);
      if (!payload.firstname || !payload.email) { showFail(document, 'Please fill required fields.'); return; }
      if (!payload.captcha || !payload.captchaToken) {
        setError(form, 'Please enter the security code shown above.');
        var inp = q('.gx-captcha-input', form); if (inp) inp.focus();
        return;
      }
      var loader = q('#loader', document); if (loader) loader.classList.add('show');
      var btn = q('button[type="submit"], .contact-us__submit', form); if (btn) btn.disabled = true;
      try {
        var res = await fetch(LEAD_API, { method: 'POST', headers: { 'Content-Type': 'application/json' }, credentials: 'same-origin', body: JSON.stringify(payload) });
        var data = await res.json().catch(function () { return {}; });
        if (res.ok && data && data.ok) { form.reset(); showSuccess(document); loadCaptcha(form, state); }
        else {
          var err = (data && data.error) || '';
          if (/captcha/.test(err)) { setError(form, err === 'captcha_expired' ? 'Security code expired — a new code is shown.' : 'Incorrect code. Please try the new code.'); await loadCaptcha(form, state); }
          else if (err === 'too_many_requests') showFail(document, 'Too many attempts. Please try again in a few minutes or call +91 7710862007.');
          else showFail(document);
        }
      } catch (err2) { showFail(document); }
      finally { state.loading = false; if (loader) loader.classList.remove('show'); if (btn) btn.disabled = false; }
    });

    qa('.open-modal-btn, #demobutton, [data-open-modal]').forEach(function (btn) {
      btn.addEventListener('click', function () { setTimeout(function () { loadCaptcha(form, state); }, 180); });
    });
    qa('.send-again-btn').forEach(function (btn) {
      btn.addEventListener('click', function () { setTimeout(function () { loadCaptcha(form, state); }, 50); });
    });
  }

  function init() { var f = q('#contact-form'); if (f) bindForm(f); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
  window.addEventListener('load', function () { setTimeout(init, 250); });
})();
