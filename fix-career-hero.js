const fs = require('fs');
let html = fs.readFileSync('career/career.html', 'utf8');

// Fix hero image section - replace inline styles with CSS class
html = html.replace(
  /<div style="display:flex;justify-content:center;align-items:center;">\s*<div style="width:100%;max-width:400px;height:300px;background:linear-gradient\(135deg,var\(--blue\),var\(--orange-100\)\);border-radius:var\(--radius\);display:flex;align-items:center;justify-content:center;box-shadow:var\(--shadow-lg\);">\s*<i class="fa fa-users" style="font-size:80px;color:rgba\(255,255,255,0\.3\);"><\/i>\s*<\/div>\s*<\/div>/,
  `<div style="display:flex;justify-content:center;align-items:center;">
          <div class="career-hero-card">
            <div class="hero-icon-group">
              <div class="icon-circle small"><i class="fa fa-laptop"></i></div>
              <div class="icon-circle large"><i class="fa fa-users"></i></div>
              <div class="icon-circle"><i class="fa fa-heartbeat"></i></div>
            </div>
          </div>
        </div>`
);

// Fix job card 1 - replace inline styles with CSS classes
html = html.replace(
  /<div class="gx-career-card" style="background:#fff;border-radius:var\(--radius\);padding:24px;margin-bottom:16px;box-shadow:var\(--shadow\);border:1px solid #eef1f8;">\s*<div class="gx-career-header" style="display:flex;align-items:center;justify-content:space-between;cursor:pointer;flex-wrap:wrap;gap:16px;">\s*<div style="flex:1;min-width:200px;">\s*<h3 style="font-size:18px;font-weight:700;color:var\(--blue\);margin-bottom:4px;">Technical\/Customer Support Executive<\/h3>\s*<p style="font-size:13px;color:#666;">Attending Client's calls and addressing all their software queries in a timely manner.<\/p>\s*<\/div>\s*<div style="font-size:13px;color:#555;">\s*<p style="margin:4px 0;"><strong>Timings:<\/strong> 10am - 7pm<\/p>\s*<p style="margin:4px 0;"><strong>Location:<\/strong> Jogeshwari - West<\/p>\s*<\/div>\s*<a href="https:\/\/tinyurl\.com\/Gymex-InterviewForm" target="_blank" style="background:var\(--blue\);color:#fff;padding:10px 24px;border-radius:10px;text-decoration:none;font-size:14px;font-weight:600;display:inline-block;white-space:nowrap;">Apply Now<\/a>\s*<\/div>/,
  `<div class="gx-career-card">
          <div class="gx-career-header">
            <div>
              <h3 class="gx-job-title">Technical/Customer Support Executive</h3>
              <p class="gx-job-desc">Attending Client's calls and addressing all their software queries in a timely manner.</p>
            </div>
            <div class="gx-career-meta">
              <p><strong>Timings:</strong> 10am - 7pm</p>
              <p><strong>Location:</strong> Jogeshwari - West</p>
            </div>
            <a href="https://tinyurl.com/Gymex-InterviewForm" target="_blank" class="gx-apply-btn">Apply Now</a>
          </div>`
);

// Fix job card 1 details - replace inline styles
html = html.replace(
  /<div class="gx-career-details" style="display:none;margin-top:16px;padding-top:16px;border-top:1px solid #eef1f8;font-size:13px;color:#555;line-height:1.7;">\s*<h5 style="font-weight:700;margin-bottom:8px;">Job Responsibilities:<\/h5>\s*<ul style="padding-left:20px;margin-bottom:16px;">/,
  `<div class="gx-career-details">
            <h5>Job Responsibilities:</h5>
            <ul>`
);

// Fix skills h5 in job 1
html = html.replace(
  /<h5 style="font-weight:700;margin-bottom:8px;">Skills and Qualifications:<\/h5>\s*<ul style="padding-left:20px;margin-bottom:16px;">/,
  `<h5>Skills and Qualifications:</h5>
            <ul>`
);

// Fix job card 2 - replace inline styles with CSS classes
html = html.replace(
  /<div class="gx-career-card" style="background:#fff;border-radius:var\(--radius\);padding:24px;margin-bottom:16px;box-shadow:var\(--shadow\);border:1px solid #eef1f8;">\s*<div class="gx-career-header" style="display:flex;align-items:center;justify-content:space-between;cursor:pointer;flex-wrap:wrap;gap:16px;">\s*<div style="flex:1;min-width:200px;">\s*<h3 style="font-size:18px;font-weight:700;color:var\(--blue\);margin-bottom:4px;">Digital Marketing Executive<\/h3>\s*<p style="font-size:13px;color:#666;">Manage social media platforms, engage with online fitness communities, and generate potential leads.<\/p>\s*<\/div>\s*<div style="font-size:13px;color:#555;">\s*<p style="margin:4px 0;"><strong>Timings:<\/strong> 10am - 7pm<\/p>\s*<p style="margin:4px 0;"><strong>Location:<\/strong> Jogeshwari - West<\/p>\s*<\/div>\s*<a href="https:\/\/tinyurl\.com\/DigitalMarketingRole"\s*target="_blank"\s*style="background:var\(--blue\);color:#fff;padding:10px 24px;border-radius:10px;text-decoration:none;font-size:14px;font-weight:600;display:inline-block;white-space:nowrap;">Apply Now<\/a>\s*<\/div>/,
  `<div class="gx-career-card">
          <div class="gx-career-header">
            <div>
              <h3 class="gx-job-title">Digital Marketing Executive</h3>
              <p class="gx-job-desc">Manage social media platforms, engage with online fitness communities, and generate potential leads.</p>
            </div>
            <div class="gx-career-meta">
              <p><strong>Timings:</strong> 10am - 7pm</p>
              <p><strong>Location:</strong> Jogeshwari - West</p>
            </div>
            <a href="https://tinyurl.com/DigitalMarketingRole" target="_blank" class="gx-apply-btn">Apply Now</a>
          </div>`
);

// Fix job card 2 details - replace inline styles
html = html.replace(
  /<div class="gx-career-details" style="display:none;margin-top:16px;padding-top:16px;border-top:1px solid #eef1f8;font-size:13px;color:#555;line-height:1.7;">\s*<h5 style="font-weight:700;margin-bottom:8px;">Job Responsibilities:<\/h5>\s*<ul style="padding-left:20px;margin-bottom:16px;">/,
  `<div class="gx-career-details">
            <h5>Job Responsibilities:</h5>
            <ul>`
);

// Fix skills h5 in job 2
html = html.replace(
  /<h5 style="font-weight:700;margin-bottom:8px;">Skills & Qualifications:<\/h5>\s*<ul style="padding-left:20px;margin-bottom:16px;">/,
  `<h5>Skills & Qualifications:</h5>
            <ul>`
);

// Fix apply now link in job 2 details
html = html.replace(
  /<a href="https:\/\/tinyurl\.com\/DigitalMarketingRole" target="_blank" style="color:var\(--blue\);font-weight:600;">Apply Now<\/a>/g,
  '<a href="https://tinyurl.com/DigitalMarketingRole" target="_blank" style="color:var(--blue);font-weight:600;">Apply Now</a>'
);

// Replace jobs container with proper class
html = html.replace(
  '<div style="max-width:1000px;margin:0 auto;">',
  '<div class="career-jobs">'
);

fs.writeFileSync('career/career.html', html);
console.log('Career page fixed!');
