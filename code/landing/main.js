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

  // --- Scroll Intersection Observer (Standard Anims) ---
  const scrollSections = document.querySelectorAll(".scroll-section");
  const sectionObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const anims = entry.target.querySelectorAll('.anim');
        anims.forEach(anim => anim.classList.add('visible'));
        if (entry.target.classList.contains('anim')) {
          entry.target.classList.add('visible');
        }
        observer.unobserve(entry.target);
      }
    });
  }, { root: null, threshold: 0.15, rootMargin: "0px 0px -50px 0px" });

  scrollSections.forEach(section => sectionObserver.observe(section));
  
  setTimeout(() => {
    const heroAnims = document.querySelectorAll('.hero .anim');
    heroAnims.forEach(a => a.classList.add('visible'));
  }, 100);

  // --- Sticky Scroll Animations (Cinematic Reveal) ---
  const stickyContainers = document.querySelectorAll('.sticky-container');
  
  function handleScroll() {
    stickyContainers.forEach(container => {
      const rect = container.getBoundingClientRect();
      const containerTop = rect.top;
      const containerHeight = rect.height;
      const windowHeight = window.innerHeight;
      
      // Calculate progress between 0 and 1 while the container is scrolling past the window
      // The sticky content sticks for (containerHeight - windowHeight) pixels
      const scrollDistance = containerHeight - windowHeight;
      let progress = -containerTop / scrollDistance;
      progress = Math.max(0, Math.min(1, progress));

      // Handle Hero Sequence
      if (container.classList.contains('hero-container')) {
        const stages = container.querySelectorAll('.h-stage');
        const numStages = stages.length;
        
        stages.forEach((stage, index) => {
          const start = index * (1 / numStages);
          const end = (index + 1) * (1 / numStages);
          
          let opacity = 0;
          let scale = 1.05;

          if (progress >= start && progress <= end) {
            const localProgress = (progress - start) / (end - start);
            
            // First stage visible immediately
            if (index === 0 && localProgress < 0.25) {
                opacity = 1;
                scale = 1;
            } else if (localProgress < 0.25) {
                opacity = localProgress / 0.25;
                scale = 1.05 - (0.05 * opacity);
            } else if (localProgress >= 0.25 && localProgress <= 0.75) {
                opacity = 1;
                scale = 1;
            } else {
                opacity = 1 - ((localProgress - 0.75) / 0.25);
                scale = 1 - (0.05 * (1 - opacity));
            }
            
            if (index === numStages - 1 && progress > end - 0.05) {
              opacity = 1;
              scale = 1;
            }
          }
          
          stage.style.opacity = opacity;
          stage.style.transform = `translate(-50%, -50%) scale(${scale})`;
          
          // Disable pointer events for hidden stages to prevent unclickable buttons
          stage.style.pointerEvents = opacity > 0.5 ? 'auto' : 'none';
        });
      }

      // Handle Timeline Sequence
      if (container.classList.contains('timeline-container')) {
        const stages = container.querySelectorAll('.t-stage');
        const numStages = stages.length;
        
        stages.forEach((stage, index) => {
          // Calculate when each stage should peak
          const start = index * (1 / numStages);
          const end = (index + 1) * (1 / numStages);
          
          let opacity = 0;
          let yOffset = 20; // Starts slightly low

          if (progress >= start && progress <= end) {
            // Map the local progress (0 to 1 for this stage's chunk)
            const localProgress = (progress - start) / (end - start);
            
            // Fade in (0 -> 0.3)
            if (localProgress < 0.3) {
              opacity = localProgress / 0.3;
              yOffset = 20 * (1 - opacity);
            } 
            // Hold (0.3 -> 0.7)
            else if (localProgress >= 0.3 && localProgress <= 0.7) {
              opacity = 1;
              yOffset = 0;
            } 
            // Fade out (0.7 -> 1.0)
            else {
              opacity = 1 - ((localProgress - 0.7) / 0.3);
              yOffset = -20 * (1 - opacity);
            }
            
            // Keep the final stage visible if we scroll past
            if (index === numStages - 1 && progress > end - 0.05) {
              opacity = 1;
              yOffset = 0;
            }
          }
          
          stage.style.opacity = opacity;
          stage.style.transform = `translate(-50%, calc(-50% + ${yOffset}px))`;
        });
      }
      
      // Handle Concepts Sequence
      if (container.classList.contains('concepts-container')) {
        const stages = container.querySelectorAll('.c-stage');
        const numStages = stages.length;
        
        stages.forEach((stage, index) => {
          const start = index * (1 / numStages);
          const end = (index + 1) * (1 / numStages);
          
          let opacity = 0;
          let yOffset = 20;

          if (progress >= start && progress <= end) {
            const localProgress = (progress - start) / (end - start);
            if (localProgress < 0.25) {
              opacity = localProgress / 0.25;
              yOffset = 20 * (1 - opacity);
            } else if (localProgress >= 0.25 && localProgress <= 0.75) {
              opacity = 1;
              yOffset = 0;
            } else {
              opacity = 1 - ((localProgress - 0.75) / 0.25);
              yOffset = -20 * (1 - opacity);
            }
            
            if (index === numStages - 1 && progress > end - 0.05) {
              opacity = 1;
              yOffset = 0;
            }
          }
          
          stage.style.opacity = opacity;
          stage.style.transform = `translate(-50%, calc(-50% + ${yOffset}px))`;
        });
      }
    });
  }

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll(); // Initial trigger

  // --- Decision Simulation Logic ---
  const simulateBtn = document.getElementById("simulate-btn");
  const simulationResult = document.getElementById("simulation-result");
  
  if (simulateBtn && simulationResult) {
    simulateBtn.addEventListener("click", () => {
      simulateBtn.innerHTML = "SIMULATING... <span class='fa-solid fa-circle-notch fa-spin'></span>";
      simulateBtn.style.opacity = "0.7";
      simulateBtn.disabled = true;
      
      setTimeout(() => {
        simulateBtn.classList.add("hidden");
        simulationResult.classList.remove("hidden");
      }, 1000);
    });
  }

  // --- Auth Routing Logic ---
  const buildBtns = document.querySelectorAll('a[href="/onboarding/"]');
  buildBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      // Mock auth check: Check if user is logged in
      const isSignedIn = localStorage.getItem('alter_signed_in') === 'true';
      if (isSignedIn) {
        window.location.href = '/onboarding/';
      } else {
        window.location.href = '/auth/sign-in/';
      }
    });
  });
});
