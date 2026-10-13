# Week 1: System Architecture Blueprint & The 5-Stage Adaptive Loop

## Ticket Summary
**ID:** `ARCH-001`  
**Assignee:** Lakkshya Jha (Lead AI Architect & Backend Systems Engineer)  
**Date:** August 14, 2026  
**Status:** Closed / Resolved  

---

## Problem / Error Description
Conventional conversational AI models operate with an isolated, single-turn context window. When applied to personal digital twins, this creates fundamental failure modes:
1. **Context Amnesia:** Historical decisions, personal schedule commitments, and past milestones are lost between interactions.
2. **Homogeneous Memory Representation:** A verified ground truth (e.g., "mandatory college classes from 9 AM to 2 PM") is treated with the same confidence as a transient observation or inferred habit.
3. **Black-Box Opacity:** Users cannot audit the underlying evidence supporting AI suggestions.

---

## Relevant Context
The objective of project *Alter* is to build a personal digital replica that learns a user's habits, commitments, and decision tendencies over time. To avoid monolithic coupling, the system must separate memory persistence, vector retrieval, and inference generation into distinct, testable modules.

---

## Key Observation & Root Cause Analysis
Attempting to fine-tune a large language model on personal logs is computationally prohibitive and risks catastrophic forgetting. A **Retrieval-Augmented Personalization Architecture** is superior: storing memories in a structured database and dynamically retrieving relevant episodic context into the prompt context for inference.

---

## Solution
1. **Engineered the 5-Stage Adaptive Loop:**
   $$\textbf{Remember} \longrightarrow \textbf{Understand} \longrightarrow \textbf{Predict} \longrightarrow \textbf{Adapt} \longrightarrow \textbf{Learn}$$
   - **Remember:** Ingest raw episodic experiences and index them with temporal and categorical metadata.
   - **Understand:** Extract semantic constants (commitments) and aggregate statistical behavioural tendencies.
   - **Predict:** Simulate likely user actions given a hypothetical dilemma using vector similarity over historical memories.
   - **Adapt:** Present recommendations tailored to current energy levels and schedule constraints.
   - **Learn:** Record user acceptance/rejection to calibrate future confidence parameters.
2. **Defined Subsystem Boundaries:**
   - **Interaction API Gateway (`code/src/main.py`):** REST routes accepting queries and scenarios.
   - **Memory Persistence Layer (`code/src/database.py`, `models.py`):** Relational storage supporting fast filtered queries.
   - **Reasoning & Simulation Engine:** Embedding-based distance ranking against historical vectors.

---

## Because
Decoupling the architecture into explicit modules allows the memory store and ranking algorithms to be developed, unit-tested, and optimized independently without requiring complex cloud-hosted model infrastructure.
