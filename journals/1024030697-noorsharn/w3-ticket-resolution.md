# Week 3: Resolving Absolute Asset Paths & Links for Local Viewing

## Ticket Summary
**ID:** `UI-003`  
**Assignee:** Noorsharn Singh (Frontend UI/UX Engineer & Data Modeling Specialist)  
**Date:** August 30, 2026  
**Status:** Closed / Resolved  

---

## Problem / Error Description
When opening HTML landing pages directly from local file explorers (using the `file://` protocol without a running HTTP web server), all styles, scripts, and navigation links failed:

```
Failed to load resource: net::ERR_FILE_NOT_FOUND (file:///assets/css/style.css)
```

Additionally, several navigation anchor links had malformed quotation marks (such as `href="app/overview""`), preventing smooth in-browser navigation during offline reviews.

---

## Relevant Context
When serving from a domain root, absolute paths like `/assets/css/style.css` resolve to the server origin. However, under local filesystem inspection or nested staging subdirectories, leading slashes resolve to the root of the local hard drive, causing complete visual breakdown.

---

## Key Observation & Root Cause Analysis
For academic submission and local evaluation by professors, the repository must remain fully viewable offline directly from disk without demanding that evaluators run local web server processes.

---

## Solution
1. **Converted Absolute Paths to Relative Paths:**
   Replaced leading slash root references (`/assets/...`, `/landing/...`) with relative directory traversals (`./assets/...`, `../../assets/...`) based on folder depth:
   ```html
   <!-- Before: Breaks in local filesystem -->
   <link rel="stylesheet" href="/assets/css/style.css">
   <a href="/landing/app/overview">Enter Twin</a>

   <!-- After: Resolves correctly across both local and server environments -->
   <link rel="stylesheet" href="../assets/css/style.css">
   <a href="./app/overview/index.html">Enter Twin</a>
   ```
2. **Fixed Syntax & Malformed Quotation Marks:**
   Audited all HTML templates to strip trailing double quotes and normalize HTML attribute quotes.

---

## Because
Using relative paths ensures that HTML documentation and prototype interfaces are completely portable and viewable across any directory structure, local file explorer, or cloud staging domain.
