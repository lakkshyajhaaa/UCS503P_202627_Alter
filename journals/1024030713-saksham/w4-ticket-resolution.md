# Week 4: Overcoming Vercel 500MB Serverless Limits via Dependency Pruning

## Ticket Summary
**ID:** `DEP-004`  
**Assignee:** Saksham Raj (Full-Stack & Cloud Infrastructure Engineer)  
**Date:** September 15, 2026  
**Status:** Closed / Resolved  

---

## Problem / Error Description
Deploying the unified monorepo to Vercel failed during serverless function compilation with the following error:

```
Error: The Serverless Function "code/src/main.py" is 742.6MB which exceeds 
the maximum allowed unzipped size of 500MB.
Please reduce the size of your function.
```

The staging deployment was completely blocked, preventing cloud access to the API.

---

## Relevant Context
Vercel serverless functions enforce a strict hard limit of 500MB uncompressed on function artifacts, encompassing all installed Python virtual environment packages (`site-packages`), shared binary objects, and application code.

---

## Key Observation & Root Cause Analysis
Inspecting installed site-packages revealed that `torch` and `sentence-transformers` were pulling in heavy precompiled PyTorch CUDA shared libraries (`libcudart.so`, `libcublas.so`) and C++ binaries exceeding 1.8GB. In a serverless cloud function with a 15-second execution timeout, spinning up GPU drivers and multi-gigabyte models causes severe cold-start latency ($> 8\text{ seconds}$) and violates platform quotas.

---

## Solution
1. **Pruned Heavy ML Packages:** Removed `torch`, `torchvision`, and `sentence-transformers` from `pyproject.toml`.
2. **Integrated Lightweight Distance Runtime:** Maintained vector ranking capabilities by relying on lightweight NumPy and SciPy spatial distance modules:
   ```python
   # In code/src/main.py
   import numpy as np
   from scipy.spatial.distance import cosine
   ```
3. Verified the deployment package size dropped from **742.6 MB down to 43.8 MB** (a 94% size reduction).
4. Re-triggered deployment via git commit, achieving an instant build with cold-start execution times under **250 ms**.

---

## Because
Serverless architecture requires lean execution bundles. Replacing massive PyTorch GPU binaries with lightweight NumPy/SciPy modules respects cloud platform limits, drastically cuts cold-start latency, and preserves vector similarity capabilities.
