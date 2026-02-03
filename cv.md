---
layout: page
title: CV
---

<h1 style="font-size: 3.5rem; margin-bottom: 0.3rem;">
  신중원 <span style="font-size: 2rem;">– JoongWon SHIN</span>
</h1>

**SNU CSE Undergraduate**

**Email**: [leodal@snu.ac.kr](mailto:leodal@snu.ac.kr)  
**GitHub**: [joongwon0204](https://github.com/joongwon0204)  
**Website**: [joongwon0204.github.io](https://joongwon0204.github.io)

---

## Education
**[Seoul National University](https://www.snu.ac.kr/index.html)**,
B.S. in **[Computer Science and Engineering](https://cse.snu.ac.kr)**, 2022–Present (Military service: 2023–2024)

---

## Projects

<div style="height: 12px;"></div>

{% assign projects = site.categories.project | sort: "date" | reverse %}
<ul class="cv-posts">
    {% for post in projects %}
        <li>
            <div class="cv-post">
                <span class="post-date">{{ post.date | date: "%Y.%m" }}</span>
                <h3 class="post-title">
                <a href="{{ post.url }}">
                    {{ post.title }}
                </a>
                </h3>
                {{ post.subtitle }}
            </div>
        </li>
    {% endfor %}
</ul>

---

## Skills
- **Languages:** C++, Java, Python, Swift
- **Interests:** Data / AI, Architecture

---

## Awards & Scholarships
**National Science and Engineering Undergraduate Scholarship (South Korea)**  
Merit-based national scholarship, 2022–Present
