/* Adapted from Codrops TextRepetitionEffect, demo 3 (MIT); see third_party/. */
const container = document.querySelector("[data-signal-repetition]");

if (container) {
  const title = container.querySelector(".signal-repetition__title");
  const line = container.querySelector(".signal-repetition__line");
  const main = container.querySelector("[data-repetition-main]");

  if (title && line && main) {
    // Preserve demo 3's nine layers, 14% displacement steps, and staggered opacity.
    const layers = [];
    for (const direction of [1, -1]) {
      for (let distance = 4; distance > 0; distance--) {
        const element = main.cloneNode(true);
        element.removeAttribute("data-repetition-main");
        line.insertBefore(element, main);
        layers.push({ element, offset: direction * distance * 14, delay: (distance - 1) * 0.08 });
      }
    }

    let frame = 0;
    let disposed = false;
    let measuredWidth = 0;
    let measuredHeight = 0;
    let mobileLayoutActive = false;
    const mobileLayout = window.matchMedia("(max-width: 760px)");
    const clamp = value => Math.min(1, Math.max(0, value));

    function fitTitle() {
      const width = container.clientWidth;
      if (!width) return;
      // Measure the rendered glyphs, including the actual loaded font and tracking.
      mobileLayoutActive = mobileLayout.matches;

      const parts = [...main.querySelectorAll(mobileLayoutActive
        ? ".signal-repetition__given-part, .signal-repetition__name-part:last-child"
        : ".signal-repetition__name-part")];
      const fontSize = parseFloat(getComputedStyle(title).fontSize);
      const textWidth = Math.max(...parts.map(part => {
        const range = document.createRange();
        range.selectNodeContents(part);
        return range.getBoundingClientRect().width;
      }));
      if (textWidth > 0) title.style.fontSize = `${fontSize * width * 0.94 / textWidth}px`;
      measuredWidth = width;
      measuredHeight = container.clientHeight;
      scheduleRender();
    }

    function renderScroll() {
      frame = 0;
      if (disposed) return;
      const bounds = container.getBoundingClientRect();
      // Start flat at the page top and reveal only the opening half as the user scrolls.
      const distance = Math.max(1, bounds.height * 0.975375);
      const progress = clamp(window.scrollY / distance);
      const time = progress * 1.24;

      for (const { element, offset, delay } of layers) {
        const amount = clamp(time - delay);
        element.style.transform = `translate3d(0, ${offset * amount}%, 0)`;
        element.style.opacity = String(amount);
      }
    }

    function scheduleRender() {
      if (!disposed && !frame) frame = window.requestAnimationFrame(renderScroll);
    }

    function onResize() {
      if (container.clientWidth !== measuredWidth || container.clientHeight !== measuredHeight || mobileLayout.matches !== mobileLayoutActive) fitTitle();
      else scheduleRender();
    }

    const resizeObserver = "ResizeObserver" in window ? new ResizeObserver(onResize) : null;

    function onPageHide(event) {
      window.cancelAnimationFrame(frame);
      frame = 0;
      if (event.persisted) return;
      disposed = true;
      resizeObserver?.disconnect();
      window.removeEventListener("scroll", scheduleRender);
      window.removeEventListener("resize", onResize);
      window.removeEventListener("pageshow", scheduleRender);
      window.removeEventListener("pagehide", onPageHide);
    }

    window.addEventListener("scroll", scheduleRender, { passive: true });
    window.addEventListener("resize", onResize);
    window.addEventListener("pageshow", scheduleRender);
    window.addEventListener("pagehide", onPageHide);
    resizeObserver?.observe(container);
    fitTitle();
    document.fonts?.load('100px "Archivo Black"', main.textContent).then(() => {
      if (!disposed) fitTitle();
    }).catch(() => {
      // The visible heading still works with the CSS fallback font.
    });
  }
}
