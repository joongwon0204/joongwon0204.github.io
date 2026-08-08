---
layout: signal
permalink: /
title: "JoongWon Shin"
description: "Undergraduate student in Computer Science and Engineering at Seoul National University, interested in hardware–software co-design, AI accelerators, and efficient LLM inference."
redirect_from:
  - /about/
  - /about.html
---

<div class="signal-shell signal-home">
  <section class="signal-hero signal-reveal" data-signal-field aria-labelledby="home-title">
    <div class="signal-hero__copy">
      <p class="signal-hero__eyebrow">PORTFOLIO</p>
      <h1 id="home-title"><span>JoongWon</span><span>Shin</span></h1>
      <p class="signal-hero__role">JoongWon Shin · 신중원</p>
      <p class="signal-hero__intro">I am an undergraduate student in Computer Science and Engineering at Seoul National University. My current interests include hardware–software co-design for AI systems, AI accelerators, and efficient LLM inference.</p>
      <p class="signal-hero__meta" aria-label="Contact links">
        {% if site.author.email %}
          <a class="signal-hero__contact" href="mailto:{{ site.author.email }}" aria-label="Email JoongWon Shin">
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path d="M3.75 5.75h16.5v12.5H3.75z" />
              <path d="m4.5 6.5 7.5 6 7.5-6" />
            </svg>
            <span>Email</span>
          </a>
        {% endif %}
        {% if site.author.github %}
          <a class="signal-hero__contact signal-hero__contact--github" href="https://github.com/{{ site.author.github }}" rel="me" aria-label="GitHub profile of JoongWon Shin">
            <svg viewBox="0 0 24 24" aria-hidden="true">
              <path d="M12 2.75a9.25 9.25 0 0 0-2.92 18.03c.46.08.63-.2.63-.45v-1.78c-2.58.56-3.12-1.1-3.12-1.1-.42-1.07-1.03-1.36-1.03-1.36-.84-.58.06-.57.06-.57.93.07 1.42.96 1.42.96.83 1.42 2.17 1.01 2.7.77.08-.6.32-1.01.59-1.24-2.06-.23-4.23-1.03-4.23-4.57 0-1.01.36-1.84.95-2.49-.1-.23-.41-1.18.09-2.46 0 0 .78-.25 2.54.95A8.8 8.8 0 0 1 12 7.07a8.8 8.8 0 0 1 2.32.31c1.76-1.2 2.53-.95 2.53-.95.51 1.28.2 2.23.1 2.46.59.65.95 1.48.95 2.49 0 3.55-2.18 4.33-4.25 4.56.34.29.63.85.63 1.72v2.67c0 .25.17.54.64.45A9.25 9.25 0 0 0 12 2.75Z" />
            </svg>
            <span>GitHub</span>
          </a>
        {% endif %}
      </p>
    </div>

    <div class="signal-hero__visual" aria-label="Circuit-board profile graphic">
      <div class="signal-hero__image-wrap">
        <img class="signal-hero__image" src="{{ '/images/profile.png' | relative_url }}" alt="Abstract circuit-board pattern illuminated in violet, blue, and cyan">
      </div>
    </div>
    {% include signal-circuit.html class="signal-hero__traces" %}
  </section>

  <section class="signal-section signal-research-section signal-reveal" id="research" aria-labelledby="research-title">
    <div class="signal-research">
      <div class="signal-research__copy">
        <p class="signal-kicker">01 / RESEARCH INTEREST</p>
        <h2 id="research-title">Research<br>Interest</h2>
        <p class="signal-section-head__intro">My interests sit across the hardware–software boundary of modern AI systems.</p>
        <ul class="signal-research__legend" aria-label="Research interest legend">
          <li>
            <button type="button" data-signal-legend="codesign" aria-controls="research-codesign" aria-pressed="false"><i aria-hidden="true"></i>Hardware–Software Co-Design</button>
          </li>
          <li>
            <button type="button" data-signal-legend="accelerators" aria-controls="research-accelerators" aria-pressed="false"><i aria-hidden="true"></i>AI Accelerators</button>
          </li>
          <li>
            <button type="button" data-signal-legend="inference" aria-controls="research-inference" aria-pressed="false"><i aria-hidden="true"></i>Efficient LLM Inference</button>
          </li>
        </ul>
      </div>

      <div class="signal-research__map" data-signal-field>
        <svg class="signal-research__routes" viewBox="0 0 640 430" aria-hidden="true">
          <defs>
            <linearGradient id="signal-route-codesign-fade" gradientUnits="userSpaceOnUse" x1="320" y1="216" x2="320" y2="108">
              <stop class="signal-route-stop--focus" offset="0" />
              <stop class="signal-route-stop--muted" offset="1" />
            </linearGradient>
            <linearGradient id="signal-route-accelerators-fade" gradientUnits="userSpaceOnUse" x1="320" y1="216" x2="160" y2="320">
              <stop class="signal-route-stop--focus" offset="0" />
              <stop class="signal-route-stop--muted" offset="1" />
            </linearGradient>
            <linearGradient id="signal-route-inference-fade" gradientUnits="userSpaceOnUse" x1="320" y1="216" x2="480" y2="320">
              <stop class="signal-route-stop--focus" offset="0" />
              <stop class="signal-route-stop--muted" offset="1" />
            </linearGradient>
          </defs>
          <path data-signal-route="codesign" d="M320 108 L320 216" />
          <path data-signal-route="accelerators" d="M160 320 L320 216" />
          <path data-signal-route="inference" d="M480 320 L320 216" />
          <circle cx="320" cy="216" r="5" />
        </svg>

        <button class="signal-node signal-node--codesign" id="research-codesign" type="button" data-signal-node="codesign" aria-pressed="false">
          <span class="signal-node__inner">Hardware–Software Co-Design</span>
        </button>
        <button class="signal-node signal-node--accelerators" id="research-accelerators" type="button" data-signal-node="accelerators" aria-pressed="false">
          <span class="signal-node__inner">AI Accelerators</span>
        </button>
        <button class="signal-node signal-node--inference" id="research-inference" type="button" data-signal-node="inference" aria-pressed="false">
          <span class="signal-node__inner">Efficient LLM Inference</span>
        </button>
      </div>
    </div>
  </section>

  <section class="signal-section signal-reveal" id="experiences" aria-labelledby="experiences-title">
    <header class="signal-section-head">
      <div>
        <p class="signal-kicker">02 / EXPERIENCES</p>
        <h2 id="experiences-title">Experiences</h2>
      </div>
      <p class="signal-section-head__aside">RESEARCH · HONOR</p>
    </header>

    <div class="signal-experience-list">
      {% for experience in site.data.experiences limit:3 %}
        <a class="signal-experience-row" data-experience-type="{{ experience.type_slug }}" href="{{ experience.url | relative_url }}">
          <span class="signal-experience-row__period">{{ experience.period }}</span>
          <span class="signal-experience-row__content">
            <span class="signal-experience-row__organization">{{ experience.organization }}</span>
            <h3>{{ experience.title }}</h3>
            <p>{{ experience.summary }}</p>
          </span>
          <span class="signal-experience-row__type">{{ experience.type }}</span>
          <span class="signal-experience-row__arrow" aria-hidden="true">→</span>
        </a>
      {% endfor %}
    </div>
    <a class="signal-more-link" href="{{ '/projects/' | relative_url }}">Open all experiences <span aria-hidden="true">→</span></a>
  </section>

  <section class="signal-section signal-reveal" aria-labelledby="notes-title">
    <header class="signal-section-head">
      <div>
        <p class="signal-kicker">03 / NOTES</p>
        <h2 id="notes-title">Notes</h2>
      </div>
      <p class="signal-section-head__aside">PROJECT LOGS · STUDY</p>
    </header>

    <div class="signal-note-list">
      {% for post in site.posts limit:3 %}
        <a class="signal-note-row" href="{{ post.url | relative_url }}">
          <span class="signal-note-row__index">00{{ forloop.index }}</span>
          <time class="signal-note-row__date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %d, %Y" | upcase }}</time>
          <span class="signal-note-row__title">
            <h3>{{ post.title }}</h3>
            {% if post.subtitle %}<p>{{ post.subtitle }}</p>{% endif %}
          </span>
          <span class="signal-note-row__type">{{ post.categories | first | upcase }}</span>
          <span class="signal-note-row__time">{{ post.content | number_of_words | divided_by: site.words_per_minute | plus: 1 }} MIN</span>
          <span class="signal-note-row__arrow" aria-hidden="true">→</span>
        </a>
      {% endfor %}
    </div>
    <a class="signal-more-link" href="{{ '/year-archive/' | relative_url }}">Open the notes archive <span aria-hidden="true">→</span></a>
  </section>
</div>
