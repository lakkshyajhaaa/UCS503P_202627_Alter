import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code', 'landing'))

def get_marketing_header(prefix):
    return f"""
  <header class="header">
    <a href="{prefix}index.html" class="logo">
      <img src="{prefix}assets/logo.webp" alt="Alter" width="52" height="52">
    </a>
    <nav class="nav-pill desktop-nav">
      <a href="{prefix}index.html">Home</a>
      <a href="{prefix}how-it-works/index.html">How It Works</a>
      <a href="{prefix}features/memory/index.html">Features</a>
      <a href="{prefix}methodology/architecture/index.html">Methodology</a>
    </nav>
    <div class="header-actions desktop-nav">
      <a href="{prefix}onboarding/index.html" class="sign-in cta-small">Build Your Twin</a>
    </div>
    <button class="burger mobile-only" aria-label="Toggle menu" aria-expanded="false">
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </button>
  </header>
"""

def get_footer(prefix):
    return f"""
  <footer class="footer" style="margin-top:auto;">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="f-logo">ALTER</div>
        <div class="f-copy">&copy; 2026 Alter</div>
      </div>
      <div class="footer-links">
        <div class="f-col">
          <a href="{prefix}methodology/architecture/index.html">Methodology</a>
          <a href="{prefix}features/memory/index.html">Features</a>
        </div>
        <div class="f-col">
          <a href="{prefix}research/research-overview/index.html">Research</a>
          <a href="{prefix}documentation/index.html">Documentation</a>
        </div>
        <div class="f-col">
          <a href="{prefix}privacy/index.html">Privacy & Trust</a>
          <a href="https://github.com/lakkshyajhaaa/UCS503P_202627_Alter">GitHub</a>
        </div>
      </div>
    </div>
  </footer>
"""

def get_mobile_menu(prefix):
    return f"""
  <div class="mobile-overlay hidden"></div>
  <div class="mobile-sheet hidden">
    <nav class="mobile-nav">
      <a href="{prefix}index.html">Home</a>
      <a href="{prefix}how-it-works/index.html">How It Works</a>
      <a href="{prefix}features/memory/index.html">Features</a>
      <a href="{prefix}methodology/architecture/index.html">Methodology</a>
      <div class="mobile-divider"></div>
      <a href="{prefix}onboarding/index.html" class="sign-in-mobile">Build Your Twin</a>
    </nav>
  </div>
"""

def get_sidebar(prefix):
    return f"""
  <aside class="sidebar">
    <div class="sidebar-logo">ALTER APP</div>
    <nav class="sidebar-nav">
      <div class="sidebar-nav-group">
        <div class="sidebar-nav-title">Engine</div>
        <a href="{prefix}app/overview/index.html" class="sidebar-link">Overview</a>
        <a href="{prefix}app/decisions/simulate-decision/index.html" class="sidebar-link">Simulate Decision</a>
        <a href="{prefix}app/ask-twin/index.html" class="sidebar-link">Ask Alter</a>
      </div>
      <div class="sidebar-nav-group">
        <div class="sidebar-nav-title">Memory</div>
        <a href="{prefix}app/memory/semantic/index.html" class="sidebar-link">Semantic</a>
        <a href="{prefix}app/memory/episodic/index.html" class="sidebar-link">Episodic</a>
        <a href="{prefix}app/memory/behavioral/index.html" class="sidebar-link">Behavioral</a>
      </div>
      <div class="sidebar-nav-group">
        <div class="sidebar-nav-title">System</div>
        <a href="{prefix}app/settings/profile/index.html" class="sidebar-link">Settings</a>
        <a href="{prefix}index.html" class="sidebar-link">Back to Site</a>
      </div>
    </nav>
  </aside>
"""

def generate_marketing_html(title, path_depth):
    prefix = "../" * path_depth if path_depth > 0 else "./"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Alter</title>
  <link rel="stylesheet" href="{prefix}styles.css">
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
{get_marketing_header(prefix)}
    <div class="content-section" style="margin-top: 15vh; flex: 1;">
      <h1 class="section-title">{title}</h1>
      <p class="section-body">This page is under construction.</p>
    </div>
{get_footer(prefix)}
  </div>
{get_mobile_menu(prefix)}
  <script src="{prefix}main.js"></script>
</body>
</html>
"""

def generate_app_html(title, path_depth):
    prefix = "../" * path_depth if path_depth > 0 else "./"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Alter App</title>
  <link rel="stylesheet" href="{prefix}styles.css">
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
{get_sidebar(prefix)}
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
    # Removing 'auth/sign-in' and 'methodology/architecture' from skip list because we manually edited them and their absolute paths are broken too, except wait: if I overwrite them, I lose the mock auth logic and the architecture page content!
    # Instead, I will skip them and fix them manually.
    skip_dirs = ['assets', 'fonts', 'auth/sign-in', 'methodology/architecture', 'app/overview', 'app/decisions/simulate-decision', 'app/memory/semantic']
    
    for root, dirs, files in os.walk(BASE_DIR):
        for f in files:
            if f != 'index.html':
                continue
                
            filepath = os.path.join(root, f)
            rel_path = os.path.relpath(filepath, BASE_DIR).replace('\\', '/')
            
            if rel_path in skip_files:
                continue
            
            should_skip = False
            for d in skip_dirs:
                if rel_path.startswith(d):
                    should_skip = True
                    break
            
            if should_skip:
                continue
            
            dir_path = os.path.dirname(rel_path)
            path_depth = len(dir_path.split('/')) if dir_path else 0
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
