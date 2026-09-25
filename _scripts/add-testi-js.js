const fs = require('fs');
let html = fs.readFileSync('index/index.html', 'utf8');

// Duplicate the cards for seamless loop
const testiScript = `
    <script>
    (function() {
      // Clone cards for infinite scroll
      var track = document.querySelector('.testi-track');
      if (track) {
        var cards = track.innerHTML;
        track.innerHTML = cards + cards;
      }
      // Generate dots
      var dots = document.getElementById('testiDots');
      if (dots) {
        var total = 10;
        for (var i = 0; i < total; i++) {
          var dot = document.createElement('span');
          dot.className = 'testi-dot' + (i === 0 ? ' active' : '');
          dot.setAttribute('data-index', i);
          dots.appendChild(dot);
        }
        // Click dot to scroll
        dots.addEventListener('click', function(e) {
          if (e.target.classList.contains('testi-dot')) {
            var idx = parseInt(e.target.getAttribute('data-index'));
            var cardWidth = 380 + 24;
            track.style.animation = 'none';
            track.style.transform = 'translateX(-' + (idx * cardWidth) + 'px)';
            dots.querySelectorAll('.testi-dot').forEach(function(d) { d.classList.remove('active'); });
            e.target.classList.add('active');
            setTimeout(function() {
              track.style.animation = '';
            }, 3000);
          }
        });
      }
    })();
    </script>
`;

// Insert before closing </body>
html = html.replace('</body>', testiScript + '\n</body>');

fs.writeFileSync('index/index.html', html);
console.log('Testimonials JS added!');
