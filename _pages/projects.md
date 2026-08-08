---
layout: signal
title: "Experiences"
description: "Major academic and research experiences of JoongWon Shin."
permalink: /projects/
---

{% assign research_experiences = site.data.experiences | where: "type_slug", "research" %}
{% assign honor_experiences = site.data.experiences | where: "type_slug", "honor" %}
<section class="signal-shell signal-index">
  <header class="signal-index-head signal-reveal">
    <div class="signal-index-head__copy">
      <p class="signal-kicker">02 / EXPERIENCES</p>
      <h1>Experiences</h1>
      <p class="signal-index-head__intro">Major academic and research milestones currently documented on this site.</p>
    </div>
    {% include signal-circuit.html class="signal-index-head__circuit" %}
  </header>

  <div class="signal-work-index signal-reveal">
    <section class="signal-work-group" aria-labelledby="research-experiences-title">
      <h2 class="signal-work-group__title" id="research-experiences-title">Research Experience</h2>
      <div class="signal-experience-list signal-experience-list--archive">
        {% for experience in research_experiences %}
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
    </section>

    <section class="signal-work-group" aria-labelledby="honor-experiences-title">
      <h2 class="signal-work-group__title" id="honor-experiences-title">Honors and Scholarships</h2>
      <div class="signal-experience-list signal-experience-list--archive">
        {% for experience in honor_experiences %}
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
    </section>
  </div>
</section>
