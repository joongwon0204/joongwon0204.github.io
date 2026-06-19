---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

<ul>
{% for post in site.categories.project %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>
