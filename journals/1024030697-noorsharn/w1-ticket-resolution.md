# Week 1: Cinematic Design System Tokens & Landing Page Scaffold

## Ticket Summary
**ID:** `UI-001`  
**Assignee:** Noorsharn Singh (Frontend UI/UX Engineer & Data Modeling Specialist)  
**Date:** August 16, 2026  
**Status:** Closed / Resolved  

---

## Problem / Error Description
Initial frontend mockups exhibited inconsistent typography, arbitrary hex colors, and disjointed button styles across views. Building a cohesive digital twin experience required a centralized design token system communicating high technology, privacy, and minimalist focus.

---

## Relevant Context
"Alter" represents an intimate digital replica of the user. Standard generic SaaS dashboard themes (bright blue borders, generic card grids) do not evoke the calm, introspective aesthetic required for personal memory reflection.

---

## Key Observation & Root Cause Analysis
Hardcoding colors and typography in individual stylesheets causes maintenance bottlenecks and visual inconsistency. Centralizing CSS custom properties (variables) guarantees uniform branding across all application views.

---

## Solution
Defined the project's global design tokens and styling guidelines:

```css
:root {
  --bg-primary: #0a0a0c;
  --bg-secondary: #121216;
  --bg-card: rgba(255, 255, 255, 0.03);
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-accent: rgba(255, 255, 255, 0.18);
  
  --text-primary: #f4f4f6;
  --text-muted: #8e8e99;
  --text-accent: #e0e0e8;

  --accent-semantic: #6366f1;   /* Indigo for stable semantic facts */
  --accent-episodic: #10b981;   /* Emerald for chronological events */
  --accent-behavioral: #f59e0b; /* Amber for inferred habits */

  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --radius-md: 12px;
  --transition-smooth: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}
```

Built the single-viewport hero layout in `code/landing/index.html` featuring high-contrast typography, dark text-shadows, and smooth interactive anchor transitions.

---

## Because
Establishing CSS custom properties and color-coded memory categories early creates visual harmony across the entire client application and allows quick theme adjustments across all pages.
