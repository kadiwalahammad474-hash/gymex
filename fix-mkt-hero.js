const fs = require('fs');
let c = fs.readFileSync('marketing-management/marketing-management.html', 'utf8');

// Find old hero section and replace with staff-style hero
const heroStart = c.indexOf('<!-- HERO -->');
const heroEnd = c.indexOf('<!-- AFTER HERO') || c.indexOf('</section>', c.indexOf('sm-hero-grid') + 100);

// Get everything from <!-- HERO --> to the next section after hero
const afterHeroMarker = c.indexOf('<!-- AFTER HERO', heroStart);
let heroEndIdx;
if (afterHeroMarker >= 0) {
    heroEndIdx = afterHeroMarker;
} else {
    // Find the closing </section> of the hero section
    let depth = 0;
    let i = c.indexOf('<section', heroStart);
    for (; i < c.length; i++) {
        if (c.substring(i, i+8) === '<section') depth++;
        if (c.substring(i, i+9) === '</section>') {
            depth--;
            if (depth === 0) { heroEndIdx = i + 9; break; }
        }
    }
}

const newHero = `<!-- HERO -->
<section class="sm-hero">
<div class="sm-hero-grid">
<div>
<div class="sm-label">MARKETING MANAGEMENT SOFTWARE</div>
<h1>Gym <span class="accent">Marketing</span> Software That Attracts, Engages &amp; Retains Members</h1>
<p class="sm-desc">Gym marketing is not just about posting on social media. Gymex helps you run targeted campaigns, send automated reminders, and track which efforts bring real members.</p>
<div class="sm-hero-cta">
<button class="mm-btn mm-btn-orange magnetic-btn open-modal-btn">Get Your Free Demo <i class="fa fa-arrow-up"></i></button>
</div>
</div>
<div class="sm-hero-img">
<div style="background:linear-gradient(135deg,#e8f0fe,#dbe8ff);border-radius:20px;padding:40px;display:flex;align-items:center;justify-content:center;min-height:320px;">
<div style="text-align:center;"><i class="fa fa-bullhorn" style="font-size:80px;color:var(--blue,#028ece);opacity:0.3;"></i><p style="font-size:14px;color:var(--gray-80,#6b7589);margin-top:16px;">Marketing Management Dashboard</p></div>
</div>
</div>
</div>
</section>

`;

if (heroStart >= 0 && heroEndIdx > heroStart) {
    c = c.substring(0, heroStart) + newHero + c.substring(heroEndIdx);
}

// Also fix the stray "n" — check for standalone 'n' lines and remove
const lines = c.split('\n');
const fixedLines = lines.filter(l => l.trim() !== 'n');
c = fixedLines.join('\n');

fs.writeFileSync('marketing-management/marketing-management.html', c);
console.log('✅ Hero fixed, stray n removed');

// Verify
const v = fs.readFileSync('marketing-management/marketing-management.html', 'utf8');
console.log('Has MARKETING MANAGEMENT:', v.includes('MARKETING MANAGEMENT'));
console.log('Has Marketing Dashboard:', v.includes('Marketing Management Dashboard'));
console.log('Has stray n:', v.split('\n').some(l => l.trim() === 'n'));
