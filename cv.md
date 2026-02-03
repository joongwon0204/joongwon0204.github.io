---
layout: page
title: CV
---

# 신중원 - JoongWon SHIN

**SNU CSE Undergraduate**

**Email**: [leodal@snu.ac.kr](mailto:leodal@snu.ac.kr)  
**GitHub**: [joongwon0204](https://github.com/joongwon0204)  
**Website**: [joongwon0204.github.io](https://joongwon0204.github.io)

---

## Education
**[Seoul National University](https://www.snu.ac.kr/index.html)**, [College of Engineering](https://eng.snu.ac.kr/snu/main/main.do)  
B.S. in **[Computer Science and Engineering](https://cse.snu.ac.kr)**, 2022–Present (Military service: 2023–2024)

---

## Projects


{% assign projects = site.categories.project | sort: "date" | reverse %}
<ul class="cv-posts">
    {% for post in projects %}
        <li>
            <div class="cv-post">
                <h3 class="post-title">
                <a href="{{ post.url }}">
                    {{ post.title }}
                </a>
                </h3>
                {{ post.subtitle }}
                <span class="post-date">{{ post.date | "%Y.%m" }}</span>
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
