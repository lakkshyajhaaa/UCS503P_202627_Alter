import os
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code', 'landing'))

custom_files = [
    'index.html',
    'auth/sign-in/index.html',
    'methodology/architecture/index.html',
    'app/overview/index.html',
    'app/decisions/simulate-decision/index.html',
    'app/memory/semantic/index.html'
]

def fix_file(rel_path):
    filepath = os.path.join(BASE_DIR, rel_path.replace('/', os.sep))
    
    dir_path = os.path.dirname(rel_path)
    path_depth = len(dir_path.split('/')) if dir_path else 0
    prefix = "../" * path_depth if path_depth > 0 else "./"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace href="/..." with href="prefix..."
    # Using a negative lookahead to not match href="//"
    content = re.sub(r'href="/(?!/)', f'href="{prefix}', content)
    
    # Replace src="/..." with src="prefix..."
    content = re.sub(r'src="/(?!/)', f'src="{prefix}', content)
    
    # For index.html specifically, we have internal page links that start with /
    # The regex handled it, e.g., href="/features/memory/" -> href="./features/memory/"
    # If the prefix is "./", that is fine for the filesystem.
    # We should make sure the trailing slash links still work. On filesystem, a trailing slash like href="./features/memory/" might look for a directory and not automatically load index.html depending on the OS/Browser!
    # On file:///, href="./features/memory/" opens the directory listing.
    # So we should ALSO replace `href=".../"` with `href=".../index.html"`
    
    # Only append index.html if it's pointing to a local directory (starts with prefix)
    # Actually, we already appended index.html in the generated template script.
    # For these custom files, let's just append index.html to any href that ends with a slash and starts with our prefix.
    def replace_slash(match):
        return match.group(0) + "index.html"
    
    # Match href="prefix/some/path/" -> href="prefix/some/path/index.html"
    # But only if it's an internal link
    content = re.sub(r'href="((\.\./|\./)[^"]*/)"', replace_slash, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed: {rel_path}")

for file in custom_files:
    fix_file(file)
