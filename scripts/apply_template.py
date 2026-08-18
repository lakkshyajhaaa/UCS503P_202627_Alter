import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code', 'landing'))

MARKETING_HEADER = """
  <header class="header">
    <a href="/" class="logo">
      <img src="/assets/logo.webp" alt="Alter" width="52" height="52">
    </a>
    <nav class="nav-pill desktop-nav">
      <a href="/">Home</a>
      <a href="/how-it-works/">How It Works</a>
      <a href="/features/memory/">Features</a>
      <a href="/methodology/architecture/">Methodology</a>
    </nav>
    <div class="header-actions desktop-nav">
      <a href="/onboarding/" class="sign-in cta-small">Build Your Twin</a>
    </div>
    <button class="burger mobile-only" aria-label="Toggle menu" aria-expanded="false">
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </button>
  </header>
"""

FOOTER = """
  <footer class="footer" style="margin-top:auto;">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="f-logo">ALTER</div>
        <div class="f-copy">&copy; 2026 Alter</div>
      </div>
      <div class="footer-links">
        <div class="f-col">
          <a href="/methodology/architecture/">Methodology</a>
          <a href="/features/memory/">Features</a>
        </div>
        <div class="f-col">
          <a href="/research/research-overview/">Research</a>
          <a href="/documentation/">Documentation</a>
        </div>
        <div class="f-col">
          <a href="/privacy/">Privacy & Trust</a>
          <a href="https://github.com/lakkshyajhaaa/UCS503P_202627_Alter">GitHub</a>
        </div>
      </div>
    </div>
  </footer>
"""

MOBILE_MENU = """
  <div class="mobile-overlay hidden"></div>
  <div class="mobile-sheet hidden">
    <nav class="mobile-nav">
      <a href="/">Home</a>
      <a href="/how-it-works/">How It Works</a>
      <a href="/features/memory/">Features</a>
      <a href="/methodology/architecture/">Methodology</a>
      <div class="mobile-divider"></div>
      <a href="/onboarding/" class="sign-in-mobile">Build Your Twin</a>
    </nav>
  </div>
"""

SIDEBAR = """
  <aside class="sidebar">
    <div class="sidebar-logo">ALTER APP</div>
    <nav class="sidebar-nav">
      <div class="sidebar-nav-group">
        <div class="sidebar-nav-title">Engine</div>
        <a href="/app/overview/" class="sidebar-link">Overview</a>
        <a href="/app/decisions/simulate-decision/" class="sidebar-link">Simulate Decision</a>
        <a href="/app/ask-twin/" class="sidebar-link">Ask Alter</a>
      </div>
      <div class="sidebar-nav-group">
        <div class="sidebar-nav-title">Memory</div>
        <a href="/app/memory/semantic/" class="sidebar-link">Semantic</a>
        <a href="/app/memory/episodic/" class="sidebar-link">Episodic</a>
        <a href="/app/memory/behavioral/" class="sidebar-link">Behavioral</a>
      </div>
      <div class="sidebar-nav-group">
        <div class="sidebar-nav-title">System</div>
        <a href="/app/settings/profile/" class="sidebar-link">Settings</a>
        <a href="/" class="sidebar-link">Back to Site</a>
      </div>
    </nav>
  </aside>
"""

def generate_marketing_html(title, path_depth):
    prefix = "../" * path_depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Alter</title>
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
  <!-- Cinematic Background -->
  <div class="bg">
    <video class="bg-video" autoplay muted loop playsinline>
      <source src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260809_012548_ef22562c-c0ae-4816-ad9d-f8922af4e6a7.mp4" type="video/mp4">
    </video>
    <div class="bg-vignette"></div>
  </div>

  <div class="page" style="min-height:100vh;">
{MARKETING_HEADER}
    <div class="content-section" style="margin-top: 15vh; flex: 1;">
      <h1 class="section-title">{title}</h1>
      <p class="section-body">This page is under construction.</p>
    </div>
{FOOTER}
  </div>
{MOBILE_MENU}
  <script src="/main.js"></script>
</body>
</html>
"""

def generate_app_html(title, path_depth):
    prefix = "../" * path_depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Alter App</title>
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
  <!-- Cinematic Background -->
  <div class="bg">
    <video class="bg-video" autoplay muted loop playsinline>
      <source src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260809_012548_ef22562c-c0ae-4816-ad9d-f8922af4e6a7.mp4" type="video/mp4">
    </video>
    <div class="bg-vignette"></div>
  </div>

  <div class="app-layout">
{SIDEBAR}
    <main class="app-content">
      <h1 class="app-page-title">{title}</h1>
      <p class="app-page-sub">Internal application routing.</p>
      
      <div class="app-panel">
        <p style="color:#aaa;">Content for {title} will be rendered here.</p>
      </div>
    </main>
  </div>
</body>
</html>
"""

def main():
    skip_files = ['index.html', 'main.js', 'styles.css']
    skip_dirs = ['assets', 'fonts', 'auth/sign-in', 'methodology/architecture']
    
    for root, dirs, files in os.walk(BASE_DIR):
        for f in files:
            if f != 'index.html':
                continue
                
            filepath = os.path.join(root, f)
            rel_path = os.path.relpath(filepath, BASE_DIR).replace('\\', '/')
            
            # Skip the main files and the ones we already specifically coded
            if rel_path in skip_files:
                continue
            
            should_skip = False
            for d in skip_dirs:
                if rel_path.startswith(d):
                    should_skip = True
                    break
            
            if should_skip:
                continue
            
            # Calculate path depth
            dir_path = os.path.dirname(rel_path)
            path_depth = len(dir_path.split('/')) if dir_path else 0
            
            # Generate title from the folder name
            folder_name = os.path.basename(dir_path).replace('-', ' ').title()
            
            if rel_path.startswith('app/') or rel_path.startswith('onboarding/'):
                html_content = generate_app_html(folder_name, path_depth)
            else:
                html_content = generate_marketing_html(folder_name, path_depth)
                
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(html_content)
            
            print(f"Updated: {rel_path}")

if __name__ == "__main__":
    main()
