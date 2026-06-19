---
layout: archive
title: "Study"
permalink: /categories/study/
author_profile: true
---

<ul>
{% for post in site.categories.study %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>
