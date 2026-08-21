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

    // Close dropdowns when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.dropdown')) {
            desktopDropdowns.forEach(function(dropdown) {
                dropdown.classList.remove('active');
            });
        }
    });
});