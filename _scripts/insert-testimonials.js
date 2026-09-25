const fs = require('fs');
let html = fs.readFileSync('index/index.html', 'utf8');

const testimonialsHTML = `
    <!-- Testimonials Section -->
    <section class="testi-section">
      <div class="container">
        <div class="testi-heading">
          <h2>What Our <span class="accent">Clients Say</span></h2>
          <p>Trusted by 500+ Gym & Fitness Studios across India</p>
        </div>
        <div class="testi-track-wrapper">
          <div class="testi-track">
            <div class="testi-card">
              <div class="testi-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
              <h4>Customer Friendly Software</h4>
              <p>Its very customer friendly. Meets the need of figures that we need on a daily basis in terms of reporting. Tracks the Business very well from manager & owner perspective.</p>
              <div class="testi-profile"><div class="testi-avatar" style="background:#e0f2fe;color:#028ece;">RJ</div><div><strong>Rashmi Joshi</strong><span>I Think Fitness</span></div></div>
            </div>
            <div class="testi-card">
              <div class="testi-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
              <h4>Easy to Use & Systematic</h4>
              <p>Software is easy to use. Approval System has removed the need for employees to send a mail for any kind of approval. All needed approvals get uploaded on the dashboard.</p>
              <div class="testi-profile"><div class="testi-avatar" style="background:#fce4ec;color:#e91e63;">M</div><div><strong>Meenakshi</strong><span>Burn Gym</span></div></div>
            </div>
            <div class="testi-card">
              <div class="testi-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
              <h4>True Asset to Our Brand</h4>
              <p>This gym software is a true asset to the Plus Fitness brand. It's a seamless all-in-one solution for managing memberships, scheduling classes, and tracking progress.</p>
              <div class="testi-profile"><div class="testi-avatar" style="background:#e8f5e9;color:#388e3c;">SL</div><div><strong>Siraj Lalani</strong><span>Master Franchisee - Plus Fitness</span></div></div>
            </div>
            <div class="testi-card">
              <div class="testi-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
              <h4>Perfect for Multi-Branch</h4>
              <p>I run a Fitness Academy and I have many branches. Gymex is a perfect software for that. I can handle all my branches sitting in any location.</p>
              <div class="testi-profile"><div class="testi-avatar" style="background:#fff3e0;color:#f57c00;">KA</div><div><strong>Kshipra Ashtewale</strong><span>IFSI Fitness Academy</span></div></div>
            </div>
            <div class="testi-card">
              <div class="testi-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
              <h4>Increased Our Business</h4>
              <p>Excellent support given by Gymex Team. Their software helps me to increase my business. Very user friendly and easy to train new staff.</p>
              <div class="testi-profile"><div class="testi-avatar" style="background:#e3f2fd;color:#1565c0;">AC</div><div><strong>Aniket Chougle</strong><span>Physc Gym</span></div></div>
            </div>
            <div class="testi-card">
              <div class="testi-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
              <h4>Best Software in India</h4>
              <p>Have recommended the software to all my friends who run gyms. I tried 4-5 Demos for gym software including Gymex & went through all the features, Gymex was the best.</p>
              <div class="testi-profile"><div class="testi-avatar" style="background:#f3e5f5;color:#7b1fa2;">IS</div><div><strong>Iqbal Sayed</strong><span>I5 Fitness</span></div></div>
            </div>
            <div class="testi-card">
              <div class="testi-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
              <h4>Best & Easy to Use</h4>
              <p>I am using this software from last 1 year and I feel that this is the best and easy to use software I have ever used in the fitness industry.</p>
              <div class="testi-profile"><div class="testi-avatar" style="background:#e0f7fa;color:#00838f;">MM</div><div><strong>Mayur Madkaikar</strong><span>DotFit Fitness</span></div></div>
            </div>
            <div class="testi-card">
              <div class="testi-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
              <h4>Very User Friendly</h4>
              <p>Amazing software, very user friendly, easy to train new staff. Members data are fully secured. It is better than other software in India.</p>
              <div class="testi-profile"><div class="testi-avatar" style="background:#fce4ec;color:#c62828;">JK</div><div><strong>Jabir Khan</strong><span>Xtreme Fitness</span></div></div>
            </div>
            <div class="testi-card">
              <div class="testi-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
              <h4>Multi-Gym Management</h4>
              <p>I manage 6 Gyms and always prefer Gymex Software. Its user friendly & easy for me to train my team. They have multiple reports which are important.</p>
              <div class="testi-profile"><div class="testi-avatar" style="background:#e8eaf6;color:#283593;">JS</div><div><strong>Javed Sayyed</strong><span>Carewell Fitness</span></div></div>
            </div>
            <div class="testi-card">
              <div class="testi-stars"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
              <h4>Using Since 2016</h4>
              <p>Glad to let you know that we are using Gymex software since 2016. It is very user-friendly and very systematic. Every time comes up with new updations.</p>
              <div class="testi-profile"><div class="testi-avatar" style="background:#e0f2fe;color:#0277bd;">SP</div><div><strong>Sonali Parab</strong><span>Curves & Cuts</span></div></div>
            </div>
          </div>
        </div>
        <div class="testi-dots" id="testiDots"></div>
      </div>
    </section>
`;

// Insert before <footer class="footer">
html = html.replace('      <footer class="footer">', testimonialsHTML + '\n      <footer class="footer">');

fs.writeFileSync('index/index.html', html);
console.log('Testimonials HTML added!');
