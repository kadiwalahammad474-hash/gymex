const fs = require('fs');
const base = 'C:/Users/Developer4/Desktop/gymexglobalwebsite';

// Read home page nav (lines 63-231)
const home = fs.readFileSync(base + '/index/index.html', 'utf8');
const homeLines = home.split('\n');
const navStart = homeLines.findIndex((l, i) => i >= 62 && l.includes('<nav class="nav"'));
const navEnd = homeLines.findIndex((l, i) => i > navStart && l.includes('</nav>'));
const homeNav = homeLines.slice(navStart, navEnd + 1).join('\n');

// Read marketing management
let content = fs.readFileSync(base + '/marketing-management/marketing-management.html', 'utf8');

// Find and replace old nav
const oldNavStart = content.indexOf('<nav class="nav" id="nav">');
const oldNavEnd = content.indexOf('</nav>', oldNavStart) + 6;

if (oldNavStart >= 0 && oldNavEnd > oldNavStart) {
    // Also check for </div> after nav
    let afterNav = content.substring(oldNavEnd, oldNavEnd + 30);
    let extraEnd = 0;
    if (afterNav.includes('</div>')) {
        extraEnd = afterNav.indexOf('</div>') + 6;
    }
    
    content = content.substring(0, oldNavStart) + homeNav + content.substring(oldNavEnd + extraEnd);
    
    fs.writeFileSync(base + '/marketing-management/marketing-management.html', content);
    console.log('✅ Nav replaced in marketing-management');
    
    // Verify
    const verify = fs.readFileSync(base + '/marketing-management/marketing-management.html', 'utf8');
    const hasMegaMenu = verify.includes('mega-menu features-mega');
    const hasContainer = verify.includes('class="container"');
    console.log('  Has mega-menu:', hasMegaMenu);
    console.log('  Has container:', hasContainer);
} else {
    console.log('❌ Could not find old nav');
}
