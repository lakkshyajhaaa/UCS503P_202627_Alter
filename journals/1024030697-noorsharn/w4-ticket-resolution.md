# Week 4: Building Dashboard Metrics & Memory Explorer UI

## Ticket Summary
**ID:** `UI-004`  
**Assignee:** Noorsharn Singh (Frontend UI/UX Engineer & Data Modeling Specialist)  
**Date:** September 14, 2026  
**Status:** Closed / Resolved  

---

## Problem / Error Description
Users had no intuitive interface to explore stored memories across the three distinct memory categories (Semantic, Episodic, Behavioural). Raw database records were opaque, and users could not distinguish between a user-verified ground truth and an unverified system inference.

---

## Relevant Context
The core UI application (`code/landing/app/`) contains:
- `overview/`: High-level metrics, active goals, recent observations.
- `memory/`: Tabbed explorer to inspect Semantic facts, Episodic event timelines, and Behavioural tendencies.

---

## Key Observation & Root Cause Analysis
Different memory categories require distinct presentation layouts:
- **Semantic:** Tagged card badges grouping verified facts and fixed schedule commitments.
- **Episodic:** A chronological event card with dates, durations, and completion markers.
- **Behavioural:** Pattern insight cards highlighting observation counts and confidence percentages.

---

## Solution
1. **Engineered Dynamic Memory Cards in `code/landing/app/memory/index.html`:**
   ```javascript
   function createMemoryCard(memory) {
     const isInferred = memory.is_inferred;
     const badgeClass = isInferred ? 'badge-inferred' : 'badge-verified';
     const badgeText = isInferred ? `Inferred (${Math.round(memory.confidence * 100)}%)` : 'Verified Ground Truth';
     
     return `
       <div class="memory-card border-subtle">
         <div class="card-header flex justify-between">
           <span class="badge ${badgeClass}">${badgeText}</span>
           <span class="card-date text-muted">${new Date(memory.created_at).toLocaleDateString()}</span>
         </div>
         <p class="card-content mt-2">${memory.content}</p>
         <div class="card-footer mt-4 flex justify-between items-center">
           <span class="tag-category">${memory.metadata?.category || 'General'}</span>
           <button class="btn-delete text-muted hover:text-red-400" onclick="deleteMemory('${memory.id}')">Delete</button>
         </div>
       </div>
     `;
   }
   ```
2. **Built Overview Metric Tiles:**
   Wired live counters for Total Memories, Predicted Accuracy ($84.2\%$), and Active Goals in `code/landing/app/overview/index.html`.

---

## Because
Presenting memories with explicit inference badges and confidence ratings provides complete transparency, fulfilling core ethical requirements and giving users clear visibility into what the AI twin has stored.
