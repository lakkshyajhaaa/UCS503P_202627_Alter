# Week 5: Decision Simulator Interface & Live API Fetch Wiring

## Ticket Summary
**ID:** `UI-005`  
**Assignee:** Noorsharn Singh (Frontend UI/UX Engineer & Data Modeling Specialist)  
**Date:** September 25, 2026  
**Status:** Closed / Resolved  

---

## Problem / Error Description
The Decision Simulator page (`code/landing/app/decisions/` and `simulate/`) needed an interactive testbed where evaluators could input hypothetical dilemmas (e.g., *"Take on an extra freelance coding assignment with evening deliverables"*) and view the Twin's decision simulation along with the exact historical reasoning behind it.

---

## Relevant Context
Decision simulation represents the primary differentiator of Alter over generic chatbots: it models what the specific user would do based on retrieved memory context rather than giving generic textbook advice.

---

## Key Observation & Root Cause Analysis
Users need responsive visual feedback during the simulation cycle:
1. An active loading spinner while the backend computes vector distances.
2. A clear confidence gauge ($82\%$).
3. A visual list of the top retrieved memories that informed the prediction.

---

## Solution
1. **Designed the Scenario Simulation View in `code/landing/app/decisions/index.html`:**
   Created an intuitive input console with prompt suggestions and scenario submission.
2. **Wired Live Asynchronous API Client:**
   ```javascript
   async function simulateScenario(scenarioPrompt) {
     const runButton = document.getElementById('run-sim-btn');
     const outputCard = document.getElementById('simulation-output');
     
     runButton.disabled = true;
     runButton.innerText = "Analyzing memories...";

     try {
       const response = await fetch('/api/simulate', {
         method: 'POST',
         headers: { 'Content-Type': 'application/json' },
         body: JSON.stringify({ scenario: scenarioPrompt })
       });

       if (!response.ok) throw new Error('API Error: ' + response.status);
       const result = await response.json();

       outputCard.innerHTML = `
         <div class="prediction-box p-4 rounded bg-card border-accent">
           <h3 class="text-xl font-bold">${result.prediction}</h3>
           <p class="text-sm text-muted mt-1">Confidence Score: <span class="text-emerald-400 font-mono">${result.confidence}%</span></p>
           <h4 class="text-md font-semibold mt-4">Supporting Historical Memories:</h4>
           <ul class="evidence-list mt-2 space-y-2">
             ${result.reasoning.map(r => `
               <li class="p-2 bg-secondary rounded text-sm border-subtle">
                 <span class="badge ${r.is_inferred ? 'badge-inferred' : 'badge-verified'} mr-2">${r.type}</span>
                 ${r.content}
               </li>
             `).join('')}
           </ul>
         </div>
       `;
     } catch (err) {
       console.error(err);
       outputCard.innerHTML = `<p class="text-red-400">Failed to connect to simulation engine. Verify backend is running.</p>`;
     } finally {
       runButton.disabled = false;
       runButton.innerText = "Simulate Decision";
     }
   }
   ```

---

## Because
Wiring the frontend interface directly to the backend simulation endpoint enables live, interactive demonstrations during the mid-semester evaluation, clearly illustrating how Alter leverages historical memories to simulate realistic human decisions.
