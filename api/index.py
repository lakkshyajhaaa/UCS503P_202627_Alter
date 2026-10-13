import sys
import os

_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_code = os.path.join(_root, 'code')
_code_src = os.path.join(_code, 'src')

for p in [_root, _code, _code_src]:
    if p and p not in sys.path:
        sys.path.insert(0, p)

try:
    from code.src.main import app
except Exception:
    try:
        from src.main import app
    except Exception:
        from main import app
