# Week 5: Serverless SQLite Bundling & Runtime sys.path Resolution

## Ticket Summary
**ID:** `DEP-005`  
**Assignee:** Saksham Raj (Full-Stack & Cloud Infrastructure Engineer)  
**Date:** September 16, 2026  
**Status:** Closed / Resolved  

---

## Problem / Error Description
Following deployment size optimization, executing requests against live staging endpoints (e.g., `GET /api/overview`) failed with HTTP 500 runtime errors in Vercel function execution logs:

```
Runtime.ImportModuleError: Unable to import module 'code/src/main': No module named 'src'
sqlite3.OperationalError: no such table: memories (unable to open database file)
```

---

## Relevant Context
In a local environment, running `uvicorn src.main:app` resolves `src` because `code` is in the local Python search path. On Vercel, the function runner invokes `code/src/main.py` directly, setting the container root path differently. Additionally, Vercel bundlers exclude `.sqlite` binary database files unless explicitly specified in configuration.

---

## Key Observation & Root Cause Analysis
1. Python's module import system could not resolve `from src.database import ...` because `code` was not in `sys.path`.
2. The pre-seeded `alter_db.sqlite` database file was omitted from the deployed function archive, resulting in a missing database at runtime.

---

## Solution
1. **Injected Dynamic Path Resolution in `code/src/main.py`:**
   ```python
   import sys
   import os

   # Add the parent directory ('code') to sys.path so 'src' packages resolve reliably on Vercel
   sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

   from src.database import get_db, engine, Base
   from src.models import Memory, MemoryType
   ```
2. **Explicitly Bundled `alter_db.sqlite` in `vercel.json`:**
   Configured `includeFiles` to ensure the pre-seeded SQLite database is included in the serverless function package:
   ```json
   {
     "functions": {
       "code/src/main.py": {
         "includeFiles": "code/src/alter_db.sqlite"
       }
     }
   }
   ```
3. Verified via curl that `GET https://alter-twin.vercel.app/api/overview` returned HTTP 200 with dynamic database counts.

---

## Because
Modifying `sys.path` programmatically and explicitly declaring database binary assets in `vercel.json` guarantees that the serverless runtime can resolve its internal modules and access the embedded SQLite database file in production.
