const fs = require('fs');
const path = require('path');

const base = 'C:/Users/Developer4/Desktop/gymexglobalwebsite';
const home = fs.readFileSync(path.join(base, 'index/index.html'), 'utf8');
const homeLines = home.split('\n');

// Extract nav from home page (lines 63-232, 0-indexed: 62-231)
const navStart = homeLines.findIndex((l, i) => i >= 62 && l.includes('<nav class="nav"'));
const navEnd = homeLines.findIndex((l, i) => i > navStart && l.includes('</nav>'));
const homeNav = homeLines.slice(navStart, navEnd + 1).join('\n');

// Extract footer from home page (lines 571-650)
const footerStart = homeLines.findIndex((l, i) => i >= 570 && l.includes('<!-- Footer -->'));
const footerEnd = homeLines.findIndex((l, i) => i > footerStart && l.includes('<!-- Footer Mobile -->'));
const homeFooter = homeLines.slice(footerStart, footerEnd).join('\n');

console.log('Home nav lines:', navStart+1, 'to', navEnd+1);
console.log('Home footer lines:', footerStart+1, 'to', footerEnd+1);
console.log('Nav length:', homeNav.length, 'chars');
console.log('Footer length:', homeFooter.length, 'chars');

// Fix each page
const pages = ['lead-management/lead-management.html', 'marketing-management/marketing-management.html'];

for (const page of pages) {
    const filePath = path.join(base, page);
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Fix header: remove <div class="container"> wrapper if present, replace nav
    // Find current nav
    const currentNavStart = content.indexOf('<div class="container"><nav class="nav"');
    const currentNavStart2 = content.indexOf('<nav class="nav"');
    const actualNavStart = currentNavStart >= 0 ? currentNavStart : currentNavStart2;
    
    if (actualNavStart >= 0) {
        const currentNavEnd = content.indexOf('</nav>', actualNavStart) + 6;
        // Also check for </div></div> after nav
        let afterNav = content.substring(currentNavEnd, currentNavEnd + 20);
        let extraEnd = 0;
        if (afterNav.trim().startsWith('</div>')) {
            extraEnd = afterNav.indexOf('</div>') + 6;
        }
        
        content = content.substring(0, actualNavStart) + homeNav + content.substring(currentNavEnd + extraEnd);
    }
    
    // Fix footer: add home footer before mobile footer
    const mobileFooterIdx = content.indexOf('<!-- Footer Mobile -->');
    if (mobileFooterIdx >= 0) {
        // Remove any existing footer content before mobile footer
        // Find the start of any existing footer (before <!-- Footer Mobile -->)
        const beforeMobile = content.substring(0, mobileFooterIdx);
        
        // Check if there's already a footer div
        const existingFooterStart = beforeMobile.lastIndexOf('<!-- Footer -->');
        if (existingFooterStart >= 0) {
            // Remove existing footer
            content = content.substring(0, existingFooterStart) + homeFooter + '\n' + content.substring(mobileFooterIdx);
        } else {
            // Add footer before mobile footer
            content = content.substring(0, mobileFooterIdx) + homeFooter + '\n' + content.substring(mobileFooterIdx);
        }
    }
    
    // Fix relative paths in nav for subdirectory pages
    content = content.replace(/href="index\.html"/g, 'href="../index/index.html"');
    content = content.replace(/href="about\.html"/g, 'href="../about/about.html"');
    content = content.replace(/href="pricing\.html"/g, 'href="../pricing/pricing.html"');
    content = content.replace(/href="blog\.html"/g, 'href="../blog/blog.html"');
    content = content.replace(/href="contact\.html"/g, 'href="../contact/contact.html"');
    content = content.replace(/href="features\.html"/g, 'href="../features/features.html"');
    
    fs.writeFileSync(filePath, content);
    console.log('\n✅ Fixed:', page);
    
    // Verify
    const verify = fs.readFileSync(filePath, 'utf8');
    const hasHomeNav = verify.includes('Marketing Management <span class="mega-badge">NEW</span>') || verify.includes('Lead Management</span>');
    const hasFooter = verify.includes('<!-- Footer -->') || verify.includes('ASK FOR DEMO');
    console.log('  Nav from home:', hasHomeNav);
    console.log('  Footer present:', hasFooter);
}
