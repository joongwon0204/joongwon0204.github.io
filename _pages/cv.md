---
layout: signal
title: "CV"
description: "Curriculum vitae of JoongWon Shin."
permalink: /cv/
redirect_from:
  - /resume
  - /resume/
---

{% assign profile = site.data.profile %}
<section class="signal-shell signal-index">
  <header class="signal-index-head signal-reveal">
    <div class="signal-index-head__copy">
      <p class="signal-kicker">04 / CURRICULUM VITAE</p>
      <h1 aria-label="{{ profile.display_name }}">{{ profile.given_name }}<br>{{ profile.family_name }}</h1>
      <p class="signal-index-head__intro">{{ profile.summary }}</p>
    </div>
    <aside class="signal-index-head__aside">
      <a class="signal-cv-download" href="{{ '/assets/cv.pdf' | relative_url }}">Download PDF&nbsp; ↗</a>
    </aside>
    {% include signal-circuit.html class="signal-index-head__circuit" %}
  </header>

  <div class="signal-cv">
    <div class="signal-timeline">
      <section class="signal-timeline__section signal-reveal" aria-labelledby="cv-education">
        <header class="signal-timeline__label">
          <span class="signal-timeline__number">01 /</span>
          <h2 id="cv-education">Education</h2>
        </header>
        <div class="signal-timeline__content">
          <article class="signal-cv-entry">
            <header class="signal-cv-entry__head">
              <h3><a href="https://www.snu.ac.kr/">Seoul National University</a></h3>
              <p class="signal-cv-entry__date">Mar. 2022 &ndash; Present</p>
            </header>
            <p class="signal-cv-entry__subtitle">Undergraduate Student in <a href="https://cse.snu.ac.kr/">Computer Science and Engineering</a></p>
            <div class="signal-cv-facts" aria-label="Academic record">
              <div><span>Completed Credits</span><strong>91</strong></div>
              <div>
                <span class="signal-gpa-toggle" tabindex="0" aria-label="Overall GPA: 4.03 out of 4.30. Hover or focus to view the official 4.00-scale equivalent: 3.88 out of 4.00.">
                  <span>Overall GPA · Hover</span>
                  <strong><span class="signal-gpa-toggle__original">4.03 / 4.30</span><span class="signal-gpa-toggle__converted">3.88 / 4.00</span></strong>
                </span>
              </div>
              <div><span>Major GPA</span><strong>4.03 / 4.30</strong></div>
            </div>
            <p class="signal-cv-entry__subtitle">Mandatory Military Service: May 2023 &ndash; Oct. 2024 (completed)</p>
          </article>
        </div>
      </section>

      <section class="signal-timeline__section signal-reveal" aria-labelledby="cv-honors">
        <header class="signal-timeline__label">
          <span class="signal-timeline__number">02 /</span>
          <h2 id="cv-honors">Honors and Scholarships</h2>
        </header>
        <div class="signal-timeline__content">
          <article class="signal-cv-entry">
            <header class="signal-cv-entry__head">
              <h3><a href="https://www.kosaf.go.kr/ko/scholar.do?pg=scholarship05_06_01">National Scholarship for Science and Engineering</a></h3>
              <p class="signal-cv-entry__date">Awarded 2022</p>
            </header>
            <p class="signal-cv-entry__subtitle">Four-year full-tuition undergraduate scholarship awarded by the Korea Student Aid Foundation</p>
          </article>
        </div>
      </section>

      <section class="signal-timeline__section signal-reveal" aria-labelledby="cv-interests">
        <header class="signal-timeline__label">
          <span class="signal-timeline__number">03 /</span>
          <h2 id="cv-interests">Research Interests</h2>
        </header>
        <div class="signal-timeline__content">
          <article class="signal-cv-entry">
            <ul>
              {% for interest in profile.research.interests %}<li>{{ interest.full_label }}</li>{% endfor %}
            </ul>
          </article>
        </div>
      </section>

      <section class="signal-timeline__section signal-reveal" id="research-experience" aria-labelledby="cv-research">
        <header class="signal-timeline__label">
          <span class="signal-timeline__number">04 /</span>
          <h2 id="cv-research">Research Experience</h2>
        </header>
        <div class="signal-timeline__content">
          <article class="signal-cv-entry">
            <header class="signal-cv-entry__head">
              <h3>Undergraduate Research Intern, <a href="https://arc.snu.ac.kr/">ARC Lab</a>, Seoul National University</h3>
              <p class="signal-cv-entry__date">Jun. &ndash; Aug. 2026</p>
            </header>
            <p class="signal-cv-entry__subtitle">Advised by Prof. <a href="https://iamjaelee.github.io/www/">Jae W. Lee</a></p>
            <ul>
              <li>Contributed to research on CXL-PNM-based hardware/software co-design for efficient LLM serving.</li>
            </ul>
          </article>
        </div>
      </section>

      <section class="signal-timeline__section signal-reveal" aria-labelledby="cv-projects">
        <header class="signal-timeline__label">
          <span class="signal-timeline__number">05 /</span>
          <h2 id="cv-projects">Projects</h2>
        </header>
        <div class="signal-timeline__content">
          <article class="signal-cv-entry">
            <header class="signal-cv-entry__head">
              <h3><a href="https://github.com/wafflestudio/22-5-team5-iOS">Wastory</a>, WaffleStudio Software Project</h3>
              <p class="signal-cv-entry__date">2025</p>
            </header>
            <ul>
              <li>Collaborated on a team-based application development project using Git-based workflows and code review.</li>
            </ul>
          </article>
        </div>
      </section>

      <section class="signal-timeline__section signal-reveal" aria-labelledby="cv-coursework">
        <header class="signal-timeline__label">
          <span class="signal-timeline__number">06 /</span>
          <h2 id="cv-coursework">Selected Coursework</h2>
        </header>
        <div class="signal-timeline__content">
          <dl class="signal-detail-list">
            <div><dt>Systems and Architecture</dt><dd>Computer Architecture, Logic Design, System Programming, Hardware Systems Design</dd></div>
            <div><dt>AI and Machine Learning</dt><dd>Computer Vision</dd></div>
            <div><dt>Algorithms and Theory</dt><dd>Data Structures, Algorithms, Discrete Mathematics, Automata Theory</dd></div>
            <div><dt>Mathematics and Statistics</dt><dd>Engineering Mathematics I&ndash;II, Statistics</dd></div>
            <div><dt>Programming and Software</dt><dd>Computer Programming, Programming Practice, Software Development Principles and Practice</dd></div>
          </dl>
        </div>
      </section>

      <section class="signal-timeline__section signal-reveal" aria-labelledby="cv-skills">
        <header class="signal-timeline__label">
          <span class="signal-timeline__number">07 /</span>
          <h2 id="cv-skills">Technical Skills</h2>
        </header>
        <div class="signal-timeline__content">
          <dl class="signal-skill-list">
            <div><dt>Programming</dt><dd>C, C++, Python, Java, Swift</dd></div>
            <div><dt>Hardware Description</dt><dd>Verilog, Amaranth</dd></div>
            <div><dt>Tools and Frameworks</dt><dd>Git, PyTorch</dd></div>
          </dl>
        </div>
      </section>
    </div>
  </div>
</section>
