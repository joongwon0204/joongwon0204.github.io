---
layout: signal
permalink: /
title: "Home"
description: "Undergraduate student in Computer Science and Engineering at Seoul National University, interested in hardware–software co-design for AI systems, efficient LLM inference, and quantitative trading."
redirect_from:
  - /about/
  - /about.html
---

{% assign profile = site.data.profile %}
<div class="signal-shell signal-home">
  <section class="signal-hero signal-reveal" aria-labelledby="home-title">
    <p class="signal-kicker">{{ profile.eyebrow | upcase }} / {{ profile.native_name }}</p>
    <h1 id="home-title" aria-label="{{ profile.display_name | escape }}">{{ profile.given_name }}<br><span>{{ profile.family_name }}</span></h1>
    <div class="signal-hero__body">
      <div class="signal-hero__portrait">
        <img src="{{ profile.image.path | relative_url }}" alt="{{ profile.image.alt | escape }}" width="460" height="460" fetchpriority="high">
      </div>
      <div class="signal-hero__copy">
        <p class="signal-hero__intro">{{ profile.intro }}</p>
        <p class="signal-hero__meta" aria-label="Contact links">
          {% if site.author.email %}
            <a class="signal-hero__contact" href="mailto:{{ site.author.email }}" aria-label="Email {{ profile.display_name }}">
              <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="M3.75 5.75h16.5v12.5H3.75z" />
                <path d="m4.5 6.5 7.5 6 7.5-6" />
              </svg>
              <span>Email</span>
            </a>
          {% endif %}
          {% if site.author.github %}
            <a class="signal-hero__contact signal-hero__contact--github" href="https://github.com/{{ site.author.github }}" rel="me" aria-label="GitHub profile of {{ profile.display_name }}">
              <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="M12 2.75a9.25 9.25 0 0 0-2.92 18.03c.46.08.63-.2.63-.45v-1.78c-2.58.56-3.12-1.1-3.12-1.1-.42-1.07-1.03-1.36-1.03-1.36-.84-.58.06-.57.06-.57.93.07 1.42.96 1.42.96.83 1.42 2.17 1.01 2.7.77.08-.6.32-1.01.59-1.24-2.06-.23-4.23-1.03-4.23-4.57 0-1.01.36-1.84.95-2.49-.1-.23-.41-1.18.09-2.46 0 0 .78-.25 2.54.95A8.8 8.8 0 0 1 12 7.07a8.8 8.8 0 0 1 2.32.31c1.76-1.2 2.53-.95 2.53-.95.51 1.28.2 2.23.1 2.46.59.65.95 1.48.95 2.49 0 3.55-2.18 4.33-4.25 4.56.34.29.63.85.63 1.72v2.67c0 .25.17.54.64.45A9.25 9.25 0 0 0 12 2.75Z" />
              </svg>
              <span>GitHub</span>
            </a>
          {% endif %}
          {% if site.author.linkedin %}
            <a class="signal-hero__contact signal-hero__contact--linkedin" href="https://www.linkedin.com/in/{{ site.author.linkedin }}" rel="me" aria-label="LinkedIn profile of {{ profile.display_name }}">
              <svg viewBox="0 0 16 16" aria-hidden="true">
                <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708C16 15.487 15.474 16 14.825 16H1.175C.526 16 0 15.487 0 14.854zm4.943 12.248V6.169H2.542v7.225zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248S2.4 3.225 2.4 3.934c0 .694.521 1.248 1.327 1.248zm3.052 8.212h2.4V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.4V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5 5 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225z" />
              </svg>
              <span>LinkedIn</span>
            </a>
          {% endif %}
        </p>
      </div>
    </div>
  </section>

  <section class="signal-section signal-reveal" id="research" aria-labelledby="research-title">
    <header class="signal-section-head">
      <div>
        <p class="signal-kicker">01 /</p>
        <h2 id="research-title">{{ profile.research.heading | escape }}</h2>
      </div>
    </header>
    <ul class="signal-interest-list">
      {% for interest in profile.research.interests %}
        <li>{{ interest.short_label }}</li>
      {% endfor %}
    </ul>
  </section>

  <section class="signal-section signal-reveal" id="experiences" aria-labelledby="experiences-title">
    {% assign experiences_archive = site.data.content_archives.experiences %}
    <header class="signal-section-head">
      <div>
        <p class="signal-kicker">02 /</p>
        <h2 id="experiences-title">Experiences</h2>
      </div>
      <p class="signal-section-head__aside">{% for group in site.data.content_groups.experiences %}{{ group.label | upcase }}{% unless forloop.last %} · {% endunless %}{% endfor %}</p>
    </header>

    <div class="signal-experience-list">
      {% assign sorted_experiences = site.experiences | sort: "date" | reverse %}
      {% for experience in sorted_experiences limit:3 %}
        {% include signal-content-row.html item=experience cell=experiences_archive.cell key="experiences" %}
      {% endfor %}
    </div>
    <a class="signal-more-link" href="{{ '/experiences/' | relative_url }}">Open all experiences <span aria-hidden="true">→</span></a>
  </section>

  <section class="signal-section signal-reveal" id="publications" aria-labelledby="publications-title">
    {% assign publications_archive = site.data.content_archives.publications %}
    <header class="signal-section-head">
      <div>
        <p class="signal-kicker">03 /</p>
        <h2 id="publications-title">Publications</h2>
      </div>
    </header>

    <div class="signal-publication-list">
      {% assign sorted_publications = site.publications | sort: "date" | reverse %}
      {% for publication in sorted_publications limit:3 %}
        {% include signal-content-row.html item=publication cell=publications_archive.cell key="publications" %}
      {% endfor %}
    </div>
    <a class="signal-more-link" href="{{ '/publications/' | relative_url }}">Open all publications <span aria-hidden="true">→</span></a>
  </section>

  <section class="signal-section signal-reveal" aria-labelledby="notes-title">
    {% assign notes_archive = site.data.content_archives.notes %}
    <header class="signal-section-head">
      <div>
        <p class="signal-kicker">04 /</p>
        <h2 id="notes-title">Notes</h2>
      </div>
      <p class="signal-section-head__aside">{% for group in site.data.content_groups.notes %}{{ group.title | upcase }}{% unless forloop.last %} · {% endunless %}{% endfor %}</p>
    </header>

    <div class="signal-note-list">
      {% assign notes_posts = site.posts | where: "key", "notes" %}
      {% for post in notes_posts limit:3 %}
        {% include signal-content-row.html item=post cell=notes_archive.cell key="notes" %}
      {% endfor %}
    </div>
    <a class="signal-more-link" href="{{ '/notes/' | relative_url }}">Open the notes archive <span aria-hidden="true">→</span></a>
  </section>
</div>
