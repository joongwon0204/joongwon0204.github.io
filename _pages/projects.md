---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

{% assign written_year = "" %}
{% for post in site.categories.project %}
{% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
{% if year != written_year %}
{% if written_year != "" %}
</ul>
{% endif %}
<h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
<ul>
{% assign written_year = year %}
{% endif %}
<li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
{% if forloop.last %}
</ul>
{% endif %}
{% endfor %}
