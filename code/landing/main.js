document.addEventListener("DOMContentLoaded", () => {
  // --- Mobile Menu Logic ---
  const burger = document.querySelector(".burger");
  const overlay = document.querySelector(".mobile-overlay");
  const sheet = document.querySelector(".mobile-sheet");
  const mobileLinks = document.querySelectorAll(".mobile-nav a");
  let menuOpen = false;

  function toggleMenu() {
    menuOpen = !menuOpen;
    if(burger) burger.setAttribute("aria-expanded", menuOpen);
    
    if (menuOpen) {
      if(overlay) overlay.classList.remove("hidden");
      if(sheet) sheet.classList.remove("hidden");
      document.body.classList.add("menu-open");
    } else {
      if(overlay) overlay.classList.add("hidden");
      if(sheet) sheet.classList.add("hidden");
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
    if (window.innerWidth > 900 && menuOpen) {
      toggleMenu();
    }
  });

  // --- Scroll Intersection Observer ---
  const scrollSections = document.querySelectorAll(".scroll-section");
  
  const sectionObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Find all .anim children within this section
        const anims = entry.target.querySelectorAll('.anim');
        anims.forEach(anim => {
          anim.classList.add('visible');
        });
        
        // If the section itself is an anim (like hero), make it visible
        if (entry.target.classList.contains('anim')) {
          entry.target.classList.add('visible');
        }
        
        // Stop observing once animated to prevent repeating
        observer.unobserve(entry.target);
      }
    });
  }, {
    root: null,
    threshold: 0.15,
    rootMargin: "0px 0px -50px 0px"
  });

  scrollSections.forEach(section => {
    sectionObserver.observe(section);
  });
  
  // Make sure hero elements animate immediately if already in view
  setTimeout(() => {
    const heroAnims = document.querySelectorAll('.hero .anim');
    heroAnims.forEach(a => a.classList.add('visible'));
  }, 100);

  // --- Decision Simulation Logic ---
  const simulateBtn = document.getElementById("simulate-btn");
  const simulationResult = document.getElementById("simulation-result");
  
  if (simulateBtn && simulationResult) {
    simulateBtn.addEventListener("click", () => {
      // Simple loading state
      simulateBtn.textContent = "Simulating...";
      simulateBtn.style.opacity = "0.7";
      simulateBtn.disabled = true;
      
      setTimeout(() => {
        simulateBtn.classList.add("hidden");
        simulationResult.classList.remove("hidden");
        
        // Smooth scroll to the result if needed
        simulationResult.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }, 1200); // 1.2s fake computation delay
    });
  }
});
