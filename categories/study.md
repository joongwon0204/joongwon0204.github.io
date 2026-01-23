---
layout: page
title: Study
permalink: /category/study/
---

{% assign posts = site.categories.study %}
{% if posts %}
<ul>
  {% for post in posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <small>{{ post.date | date: "%Y-%m-%d" }}</small>
    </li>
  {% endfor %}
</ul>
{% else %}
<p><small>아직 글 없음</small></p>
{% endif %}