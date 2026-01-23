---
layout: default
title: "Home"
heading: "활동 연혁"
subheading: "카테고리별로 정리된 타임라인"
---

{% assign posts = site.posts %}

{% for post in posts %}
  <a href="{{ post.url | relative_url }}">
    <div class="card post-item">
      <div class="meta">
        <span>{{ post.date | date: "%Y-%m-%d" }}</span>
        {% if post.categories and post.categories.size > 0 %}
          <span class="pill">{{ post.categories[0] }}</span>
        {% endif %}
      </div>

      <div class="h1">{{ post.title }}</div>

      {% if post.subtitle %}
        <div class="subtitle">{{ post.subtitle }}</div>
      {% elsif post.description %}
        <div class="subtitle">{{ post.description }}</div>
      {% endif %}
    </div>
  </a>
{% endfor %}