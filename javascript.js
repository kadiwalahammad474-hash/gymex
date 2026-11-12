document.addEventListener('DOMContentLoaded', function () {
    // Mobile menu dropdowns
    var businessTypesLink = document.getElementById('business-types-link');
    var dropdownMenu = document.getElementById('dropdown-menu');

    if (businessTypesLink && dropdownMenu) {
        businessTypesLink.addEventListener('click', function (event) {
            event.preventDefault();
            dropdownMenu.classList.toggle('show');
        });
    }

    var featuresLink = document.getElementById('features-link');
    var featuresDropdownMenu = document.getElementById('features-dropdown-menu');

    if (featuresLink && featuresDropdownMenu) {
        featuresLink.addEventListener('click', function (event) {
            event.preventDefault();
            featuresDropdownMenu.classList.toggle('show');
        });
    }

    // Desktop mega-menu dropdowns - click support
    var desktopDropdowns = document.querySelectorAll('.nav__list .dropdown');
    desktopDropdowns.forEach(function(dropdown) {
        var link = dropdown.querySelector('.nav__link');
        if (link) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                // Close other dropdowns
                desktopDropdowns.forEach(function(other) {
                    if (other !== dropdown) {
                        other.classList.remove('active');
                    }
                });
                dropdown.classList.toggle('active');
            });
        }
    });

// ════════════════════════════════════════════════════════════
    // Mobile burger menu — canonical handler (backdrop toggle).
    // Ye sirf tab active hota hai jab page pe #open-menu + #menu-backdrop hain.
    // ════════════════════════════════════════════════════════════
    var menuBackdrop = document.getElementById('menu-backdrop');
    var menuBurger = document.getElementById('open-menu');

    if (menuBackdrop && menuBurger) {
        menuBurger.addEventListener('click', function () {
            var open = menuBackdrop.classList.toggle('visible');
            menuBurger.classList.toggle('menu-animated', open);
            document.body.style.overflow = open ? 'hidden' : 'auto';
        });

        // Backdrop khud pe click = menu band
        menuBackdrop.addEventListener('click', function (e) {
            if (e.target === menuBackdrop) {
                menuBackdrop.classList.remove('visible');
                menuBurger.classList.remove('menu-animated');
                document.body.style.overflow = 'auto';
            }
        });

        // Menu ke andar kisi bhi link pe click = menu band
        menuBackdrop.querySelectorAll('.menu__link').forEach(function (link) {
            link.addEventListener('click', function () {
                menuBackdrop.classList.remove('visible');
                menuBurger.classList.remove('menu-animated');
                document.body.style.overflow = 'auto';
            });
        });
    }

    // Close dropdowns when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.dropdown')) {
            desktopDropdowns.forEach(function(dropdown) {
                dropdown.classList.remove('active');
            });
        }
    });

    // Demo modal open (global) - only if modal exists
    var demoPopup = document.getElementById('divemailpopup');
    if (demoPopup) {
        document.addEventListener('click', function(e) {
            var btn = e.target.closest('.open-modal-btn, #demobutton');
            if (btn) {
                e.preventDefault();
                demoPopup.classList.add('show');
                document.body.style.overflow = 'hidden';
            }
            if (e.target === demoPopup) {
                demoPopup.classList.remove('show');
                document.body.style.overflow = 'auto';
            }
        });
        var closeBtn = document.getElementById('close-contact-modal');
        if (closeBtn) {
            closeBtn.addEventListener('click', function() {
                demoPopup.classList.remove('show');
                document.body.style.overflow = 'auto';
            });
        }
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && demoPopup.classList.contains('show')) {
                demoPopup.classList.remove('show');
                document.body.style.overflow = 'auto';
            }
        });
    }
});

// ════════════════════════════════════════════════════════════
// Demo form (server captcha + /api/demo-lead) — har page par.
// ════════════════════════════════════════════════════════════
(function () {
    var current = document.currentScript ||
        document.querySelector('script[src*="javascript.js"]');
    if (!current || !current.src) return;

    var base = current.src.replace(/javascript\.js[^/]*$/, '');
    var script = document.createElement('script');
    script.src = base + 'js/demo-form.js?v=1';
    script.defer = true;
    document.head.appendChild(script);
})();