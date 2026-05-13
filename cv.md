---
layout: page
sideBarTitle: CV
---

<style>
  .cv {
    max-width: 900px;
    margin: 0 auto;
    color: #222;
    font-size: 0.95rem;
    line-height: 1.45;
  }

  .cv-header {
    text-align: center;
    margin-bottom: 1rem;
  }

  .cv-name {
    margin: 0 0 0.25rem;
    font-size: 2rem;
    line-height: 1.1;
  }

  .cv-contact {
    margin-top: 0.2rem;
  }

  .cv-section {
    margin-top: 1rem;
  }

  .cv-section h2 {
    margin: 0 0 0.45rem;
    padding-bottom: 0.18rem;
    border-bottom: 1px solid #222;
    font-size: 1.15rem;
    line-height: 1.25;
  }

  .cv-item-head {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 0.15rem;
    font-weight: 700;
  }

  .cv-date {
    flex: 0 0 auto;
    text-align: right;
    font-weight: 700;
  }

  .cv p {
    margin: 0.1rem 0;
  }

  .cv ul {
    margin: 0.25rem 0 0;
    padding-left: 1.2rem;
  }

  .cv li {
    margin: 0.12rem 0;
  }

  .cv-table {
    display: grid;
    grid-template-columns: max-content 1fr;
    column-gap: 0.6rem;
    row-gap: 0.25rem;
  }

  .cv-table strong {
    white-space: nowrap;
  }

  @media (max-width: 640px) {
    .cv {
      font-size: 0.9rem;
    }

    .cv-name {
      font-size: 1.65rem;
    }

    .cv-item-head {
      display: block;
    }

    .cv-date {
      text-align: left;
      font-weight: 600;
    }

    .cv-table {
      grid-template-columns: 1fr;
      row-gap: 0.1rem;
    }

    .cv-table strong {
      margin-top: 0.35rem;
    }
  }
</style>

<article class="cv">
  <header class="cv-header">
    <h1 class="cv-name">JoongWon SHIN</h1>
    <p>Seoul National University, Department of Computer Science and Engineering</p>
    <p class="cv-contact">
      Email:
      <a href="mailto:leodal@snu.ac.kr">leodal@snu.ac.kr</a>
      &nbsp;|&nbsp;
      GitHub:
      <a href="https://github.com/joongwon0204">github.com/joongwon0204</a>
    </p>
  </header>

  <section class="cv-section">
    <h2>Education</h2>
    <div class="cv-item-head">
      <span>Seoul National University</span>
      <span class="cv-date">Mar. 2022 - Present</span>
    </div>
    <p>B.S. in Computer Science and Engineering</p>
    <p>3rd year, 1st semester &nbsp;|&nbsp; Completed Credits: 72</p>
    <p>GPA: 4.04 / 4.30 &nbsp;|&nbsp; Major GPA: 4.11 / 4.30</p>
    <p>Military Service: Completed mandatory military service, May 2023 - Oct. 2024</p>
  </section>

  <section class="cv-section">
    <h2>Honors and Scholarships</h2>
    <div class="cv-item-head">
      <span>National Scholarship for Sciences and Engineering</span>
      <span class="cv-date">Awarded 2022</span>
    </div>
    <p>Four-year full-tuition undergraduate scholarship awarded by Korea Student Aid Foundation</p>
  </section>

  <section class="cv-section">
    <h2>Research Interests</h2>
    <ul>
      <li>AI accelerators and efficient AI computing</li>
      <li>Computer architecture and hardware systems</li>
      <li>AI systems and hardware-software interfaces</li>
    </ul>
  </section>

  <section class="cv-section">
    <h2>Relevant Coursework</h2>
    <div class="cv-table">
      <strong>Systems and Architecture:</strong>
      <span>Computer Architecture, Logic Design, System Programming (currently taking), Hardware Systems Design (currently taking)</span>

      <strong>AI and Vision:</strong>
      <span>Computer Vision (currently taking)</span>

      <strong>Algorithms and Theory:</strong>
      <span>Data Structures, Algorithms, Discrete Mathematics, Automata Theory</span>

      <strong>Mathematics and Statistics:</strong>
      <span>Engineering Mathematics 1-2, Statistics</span>

      <strong>Programming and Software:</strong>
      <span>Computer Programming, Programming Practice, Software Development Principles and Practice (currently taking)</span>
    </div>
  </section>

  <section class="cv-section">
    <h2>Projects</h2>
    <div class="cv-item-head">
      <span>Wastory, WaffleStudio Software Project</span>
      <span class="cv-date">2025</span>
    </div>
    <ul>
      <li>Participated in a team-based clone coding project and gained experience with Git-based collaboration, code review, and application development.</li>
    </ul>
  </section>

  <section class="cv-section">
    <h2>Technical Skills</h2>
    <div class="cv-table">
      <strong>Programming:</strong>
      <span>C, C++, Python, Java, Swift</span>

      <strong>Hardware Description:</strong>
      <span>Verilog, Amaranth</span>

      <strong>Tools/Frameworks:</strong>
      <span>Git, PyTorch</span>
    </div>
  </section>
</article>
