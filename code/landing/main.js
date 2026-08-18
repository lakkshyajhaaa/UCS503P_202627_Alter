document.addEventListener("DOMContentLoaded", () => {
  // --- Mobile Menu Logic ---
  const burger = document.querySelector(".burger");
  const overlay = document.querySelector(".mobile-overlay");
  const sheet = document.querySelector(".mobile-sheet");
  const mobileLinks = document.querySelectorAll(".mobile-nav a");
  let menuOpen = false;

  function toggleMenu() {
    menuOpen = !menuOpen;
    burger.setAttribute("aria-expanded", menuOpen);
    
    if (menuOpen) {
      overlay.classList.remove("hidden");
      sheet.classList.remove("hidden");
      document.body.classList.add("menu-open");
    } else {
      overlay.classList.add("hidden");
      sheet.classList.add("hidden");
      document.body.classList.remove("menu-open");
    }
  }

  if (burger) burger.addEventListener("click", toggleMenu);
  if (overlay) overlay.addEventListener("click", () => { if (menuOpen) toggleMenu(); });
  
  mobileLinks.forEach(link => {
    link.addEventListener("click", () => { if (menuOpen) toggleMenu(); });
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && menuOpen) toggleMenu();
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 720 && menuOpen) {
      toggleMenu();
    }
  });

  // --- Stats Count-Up Logic ---
  const statValues = document.querySelectorAll(".stat-value");
  
  // easeOutCubic function
  const easeOutCubic = (t) => 1 - Math.pow(1 - t, 3);

  const animateValue = (el, i) => {
    const target = parseFloat(el.getAttribute("data-target"));
    const suffix = el.getAttribute("data-suffix") || "";
    const decimals = parseInt(el.getAttribute("data-decimals")) || 0;
    const duration = 1500 + i * 80;
    const delay = 480 + i * 90;
    
    let startTime = null;

    // Set to 0 initially
    el.textContent = `0${decimals > 0 ? '.' + '0'.repeat(decimals) : ''}${suffix}`;

    setTimeout(() => {
      const step = (timestamp) => {
        if (!startTime) startTime = timestamp;
        const progress = Math.min((timestamp - startTime) / duration, 1);
        const easeProgress = easeOutCubic(progress);
        
        const currentValue = easeProgress * target;
        el.textContent = `${currentValue.toFixed(decimals)}${suffix}`;
        
        if (progress < 1) {
          requestAnimationFrame(step);
        } else {
          el.textContent = `${target.toFixed(decimals)}${suffix}`;
        }
      };
      requestAnimationFrame(step);
    }, delay);
  };

  if (statValues.length > 0) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          statValues.forEach((el, i) => animateValue(el, i));
          obs.disconnect(); // Only run once
        }
      });
    }, { threshold: 0.25 });
    
    observer.observe(document.querySelector(".stats"));
  }
});
