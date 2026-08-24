const fs = require('fs');
const path = require('path');

const filePath = path.join('C:/Users/Developer4/Desktop/gymexglobalwebsite', 'contact/contact.html');
let content = fs.readFileSync(filePath, 'utf8');

// Remove the grey links bar
const greyBar = /    <!-- Grey Links Bar -->\n    <div style="background:#f3f4f6;[\s\S]*?<\/div>\n\n    <section/;

if (greyBar.test(content)) {
  content = content.replace(greyBar, '\n    <section');
  fs.writeFileSync(filePath, content, 'utf8');
  console.log('Grey bar removed from contact page');
} else {
  console.log('Grey bar not found');
}
