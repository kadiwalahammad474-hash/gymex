const fs = require('fs');
let html = fs.readFileSync('business/business.html', 'utf8');

// Find form-body and remove from that point
const formIdx = html.indexOf('form-body');
if (formIdx !== -1) {
  const before = html.lastIndexOf('<div', formIdx);
  html = html.substring(0, before);
}

// Find /body and strip
const bodyEnd = html.indexOf('</body>');
if (bodyEnd !== -1) html = html.substring(0, bodyEnd);
html = html.trimEnd();

const suffix = '\n\n<!-- Demo Modal -->\n<div class="demo-modal-overlay" id="demoModal">\n  <div class="demo-modal">\n    <button class="demo-modal-close" onclick="document.getElementById(\'demoModal\').classList.remove(\'active\')">&times;</button>\n    <h2>Get Your <span style="color:var(--blue)">Free Demo</span></h2>\n    <p class="subtitle">See how Gymex can transform your gym management.</p>\n    <form action="../contactus.php" method="post">\n      <input type="hidden" name="backurl" value="">\n      <div class="form-row">\n        <div><label>First Name *</label><input type="text" name="firstname" placeholder="John" required></div>\n        <div><label>Last Name *</label><input type="text" name="lastname" placeholder="Doe" required></div>\n      </div>\n      <div class="form-row">\n        <div><label>Email *</label><input type="email" name="email" placeholder="john@example.com" required></div>\n        <div><label>Phone *</label><input type="tel" name="phonenumber" placeholder="98765 43210" required></div>\n      </div>\n      <div><label>Company / Gym Name</label><input type="text" name="company" placeholder="Your Gym Name"></div>\n      <div><label>Message</label><textarea name="message" placeholder="Tell us about your gym..."></textarea></div>\n      <button type="submit" class="submit-btn">Submit &amp; Get Free Demo <i class="fa fa-arrow-right"></i></button>\n    </form>\n  </div>\n</div>\n\n<script>\n(function(){\nvar T=document.getElementById("menu-backdrop"),b=document.getElementById("open-menu");\nif(b&&T){b.addEventListener("click",function(){T.classList.toggle("visible");b.classList.toggle("menu-animated");b.classList.remove("visible");T.classList.contains("visible")?document.body.style.overflow="hidden":document.body.style.overflow="auto"});\ndocument.body.addEventListener("click",function(e){if(e.target===T){T.classList.remove("visible");b.classList.remove("menu-animated");b.classList.add("visible");document.body.style.overflow="auto"}});\ndocument.querySelectorAll(".menu__link").forEach(function(c){c.addEventListener("click",function(){T.classList.remove("visible");b.classList.add("visible");b.classList.remove("menu-animated");document.body.style.overflow="auto"})});\n}\ndocument.querySelectorAll(".open-demo-modal").forEach(function(btn){\n  btn.addEventListener("click",function(e){e.preventDefault();document.getElementById("demoModal").classList.add("active");});\n});\nvar dm=document.getElementById("demoModal");\nif(dm){dm.addEventListener("click",function(e){if(e.target===this)this.classList.remove("active");});}\ndocument.addEventListener("keydown",function(e){if(e.key==="Escape"&&dm)dm.classList.remove("active");});\n})();\n</script>\n</body>\n</html>';

html += suffix;
fs.writeFileSync('business/business.html', html);
console.log('Business page cleaned + demo modal + menu JS added');
