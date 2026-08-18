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
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Fix the broken quote issue caused by previous script
    # href="./how-it-works/"index.html -> href="./how-it-works/index.html"
    content = re.sub(r'href="([^"]*/)"index\.html', r'href="\1index.html"', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed quotes: {rel_path}")

for file in custom_files:
    fix_file(file)
