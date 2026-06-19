---
permalink: /
title: "JoongWon SHIN"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am an undergraduate student in the Department of Computer Science and Engineering at Seoul National University.

My current interests are computer architecture, AI accelerators, efficient AI computing, and hardware-software interfaces. I am preparing to work as a full-time undergraduate research intern at Jae W. Lee Lab, SNU, in Summer 2026.

Research Interests
======

* AI accelerators and efficient AI computing
* Computer architecture and hardware systems
* AI systems and hardware-software interfaces

Recent Posts
======

<ul>
{% for post in site.posts limit:5 %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>
