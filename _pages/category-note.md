---
layout: archive
title: "Note"
permalink: /categories/note/
author_profile: true
---

<ul>
{% for post in site.categories.notes %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
{% endfor %}

{% for post in site.categories.note %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>
