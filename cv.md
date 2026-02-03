---
layout: page
title: CV
---

## Shin JoongWon
**SNU CSE Undergraduate**  
Email: leodal@snu.ac.kr  
GitHub: https://github.com/joongwon0204  
Website: https://joongwon0204.github.io

---

## Education
**Seoul National University**, College of Engineering  
B.S. in Computer Science and Engineering, 2022–Present (Military service: 2023–2024)

---

## Projects
{% assign projects = site.categories.project | sort: "date" | reverse %}
<ul>
    {% for post in projects %}
        <li>
            <div class="post">
                <h3 class="post-title">
                <a href="{{ post.url }}">
                    {{ post.title }}
                </a>
                </h3>
                <p>{{ post.subtitle }}</p>

                <span class="post-date">{{ post.date | date_to_string }}</span>

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
