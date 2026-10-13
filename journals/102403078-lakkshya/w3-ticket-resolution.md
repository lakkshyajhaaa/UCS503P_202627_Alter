# Week 3: 60-Day Dataset Ingestion Engine & Rule Extraction

## Ticket Summary
**ID:** `INGEST-003`  
**Assignee:** Lakkshya Jha (Lead AI Architect & Backend Systems Engineer)  
**Date:** August 28, 2026  
**Status:** Closed / Resolved  

---

## Problem / Error Description
The raw dataset collected in `dataset/continuous_60_day_ai_schedule_dataset.csv` contains tabular logs of student activities, duration, distraction ratings, and task completion flags. To be utilized by the AI Twin, tabular entries must be transformed into natural language episodic narratives, declarative semantic rules, and statistical behavioral tendencies.

---

## Relevant Context
An AI assistant cannot effectively simulate user choices from raw tabular columns like `is_fixed_schedule=1, energy_level_1_5=4`. The system requires natural language formulations that can be transformed into semantic vector embeddings for contextual retrieval.

---

## Key Observation & Root Cause Analysis
A multi-stage transformation pipeline is needed to extract all three memory tiers from the tabular data:
1. **Episodic:** Row-by-row narrative sentences capturing time, activity, category, and completion state.
2. **Semantic:** Fixed schedule filters identifying mandatory commitments (classes, commutes).
3. **Behavioural:** Aggregated statistical analysis (e.g., completion rate correlation with distraction levels).

---

## Solution
Implemented the batch ingestion engine in `code/src/ingest.py`:

```python
import pandas as pd
import os
from src.database import SessionLocal
from src.models import Memory, MemoryType

def ingest_data():
    db = SessionLocal()
    df = pd.read_csv('dataset/continuous_60_day_ai_schedule_dataset.csv')
    memories_to_add = []

    # 1. Episodic: Chronological narrative generation
    for _, row in df.iterrows():
        completed = "completed" if row['task_completed'] == 1 else "did not complete"
        content = f"On {row['date']} ({row['day_of_week']}) from {row['time_start']} to {row['time_end']}, I {completed} '{row['activity']}' ({row['category']})."
        memories_to_add.append({
            "memory_type": MemoryType.EPISODIC,
            "content": content,
            "metadata_": {"date": row['date'], "duration": row['duration_min'], "energy": row['energy_level_1_5']},
            "is_inferred": False, "confidence": 1.0
        })

    # 2. Semantic: Invariable commitments
    for activity in df[df['is_fixed_schedule'] == 1]['activity'].unique():
        memories_to_add.append({
            "memory_type": MemoryType.SEMANTIC,
            "content": f"My schedule requires mandatory fixed time for: {activity}.",
            "metadata_": {"category": "Fixed Commitment"},
            "is_inferred": False, "confidence": 1.0
        })

    # 3. Behavioural: Empirical patterns
    high_dist = df[df['distraction_level'] == 'High']
    if not high_dist.empty:
        rate = high_dist['task_completed'].mean() * 100
        memories_to_add.append({
            "memory_type": MemoryType.BEHAVIORAL,
            "content": f"When my distraction level is High, my task completion rate drops to {rate:.1f}%.",
            "metadata_": {"insight_type": "Distraction Impact"},
            "is_inferred": True, "confidence": 0.85
        })
```

Batch-inserted records in chunks of 64 with 384-dimensional vector embeddings directly into `alter_db.sqlite`.

---

## Because
Automated parsing bridges the gap between raw behavioral timeseries logs and cognitive AI memory representations, populating the twin with grounded historical context before live user interactions.
