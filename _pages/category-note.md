---
layout: archive
title: "Note"
permalink: /categories/note/
author_profile: true
---

{% for post in site.categories.notes %}
  {% include archive-single.html %}
{% endfor %}

{% for post in site.categories.note %}
  {% include archive-single.html %}
{% endfor %}
