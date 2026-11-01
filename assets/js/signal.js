(function () {
  "use strict";

  var root = document.documentElement;
  root.classList.remove("no-js");
  root.classList.add("signal-js");

  var menuButton = document.querySelector("[data-signal-menu]");
  var navigation = document.querySelector("[data-signal-nav]");
  function closeMenu() {
    if (!menuButton || !navigation) return;
    menuButton.setAttribute("aria-expanded", "false");
    document.body.classList.remove("signal-nav-open");
  }

  if (menuButton && navigation) {
    menuButton.addEventListener("click", function () {
      var isOpen = menuButton.getAttribute("aria-expanded") === "true";
      menuButton.setAttribute("aria-expanded", String(!isOpen));
      document.body.classList.toggle("signal-nav-open", !isOpen);
    });

    navigation.addEventListener("click", function (event) {
      if (event.target.closest("a")) closeMenu();
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") closeMenu();
    });
  }

  var filterGroups = Array.prototype.slice.call(document.querySelectorAll("[data-signal-filter-group]"));
  filterGroups.forEach(function (group) {
    var selector = group.getAttribute("data-signal-filter-target");
    var scope = group.parentElement || document;
    var controls = Array.prototype.slice.call(group.querySelectorAll("[data-signal-filter]"));
    var items = selector ? Array.prototype.slice.call(scope.querySelectorAll(selector)) : [];
    var sections = Array.prototype.slice.call(scope.querySelectorAll("[data-signal-filter-section]"));

    function applyFilter(value) {
      controls.forEach(function (control) {
        control.setAttribute("aria-pressed", String(control.getAttribute("data-signal-filter") === value));
      });

      items.forEach(function (item) {
        var category = item.getAttribute("data-signal-category");
        item.hidden = value !== "all" && category !== value;
      });

      sections.forEach(function (section) {
        var sectionItems = selector ? Array.prototype.slice.call(section.querySelectorAll(selector)) : [];
        section.hidden = sectionItems.length > 0 && sectionItems.every(function (item) { return item.hidden; });
      });
    }

    controls.forEach(function (control) {
      control.addEventListener("click", function () {
        applyFilter(control.getAttribute("data-signal-filter"));
      });
    });

    applyFilter("all");
  });

  var gpaHover = document.querySelector(".signal-gpa-toggle");
  if (gpaHover) {
    gpaHover.addEventListener("pointerdown", function (event) {
      if (event.pointerType === "mouse") event.preventDefault();
    });
  }

  var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var reveals = Array.prototype.slice.call(document.querySelectorAll(".signal-reveal"));
  if (prefersReducedMotion || !("IntersectionObserver" in window)) {
    reveals.forEach(function (element) { element.classList.add("is-visible"); });
  } else {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8%", threshold: 0.08 });
    reveals.forEach(function (element) { observer.observe(element); });
  }
})();
