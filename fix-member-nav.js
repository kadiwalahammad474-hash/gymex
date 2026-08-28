const fs = require('fs');
const base = 'C:/Users/Developer4/Desktop/gymexglobalwebsite';

// Read home page - extract nav (lines 63 to </nav>)
const home = fs.readFileSync(base + '/index/index.html', 'utf8');
const homeLines = home.split('\n');
const navStart = homeLines.findIndex((l, i) => i >= 62 && l.includes('<nav class="nav"'));
const navEnd = homeLines.findIndex((l, i) => i > navStart && l.trim() === '</nav>');
const homeNav = homeLines.slice(navStart, navEnd + 1).join('\n');

// Read member management
let content = fs.readFileSync(base + '/member-management/member-management.html', 'utf8');

// Find old nav start and end
const oldNavStart = content.indexOf('<nav class="nav" id="nav">');
const oldNavEnd = content.indexOf('</nav>', oldNavStart) + 6;

if (oldNavStart >= 0 && oldNavEnd > oldNavStart) {
    content = content.substring(0, oldNavStart) + homeNav + content.substring(oldNavEnd);
    fs.writeFileSync(base + '/member-management/member-management.html', content);
    console.log('✅ Nav replaced');
    
    // Verify
    const v = fs.readFileSync(base + '/member-management/member-management.html', 'utf8');
    console.log('Has logo2.png:', v.includes('logo2.png'));
    console.log('Has Gymex-logo-wit:', v.includes('Gymex-logo-wit'));
    console.log('Has container class:', v.includes('class="container"'));
    console.log('Has nav__logo-links:', v.includes('nav__logo-links-container'));
} else {
    console.log('❌ Nav not found');
}
