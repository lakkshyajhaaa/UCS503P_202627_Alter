# Engineering Journal — Lakkshya Jha

**Student Name:** Lakkshya Jha  
**Roll Number:** 102403078 (Alt: 1024030708)  
**Group:** 3C52 — BE Third Year, Computer Engineering  
**Course:** Software Engineering (UCS503 / UCS503P)  
**Project:** Alter — Personal Digital Twin  
**Assigned Role:** **Lead AI Architect & Backend Systems Engineer**

---

## Assigned Engineering Responsibilities
- **System Architecture & Core Logic:** Formalizing the 5-stage adaptive cycle (*Remember, Understand, Predict, Adapt, Learn*) and modular component interfaces separating Memory, Retrieval, and Inference.
- **Relational & Vector Data Modeling:** Designing the unified `Memory` schema in SQLAlchemy (`models.py`), mapping tripartite memory types (Semantic, Episodic, Behavioural), and optimizing embedding persistence on SQLite.
- **Ingestion Pipeline Engineering:** Developing the batch ingestion engine (`ingest.py`) to process the 60-day behavioral schedule dataset (`continuous_60_day_ai_schedule_dataset.csv`), generating structured episodic narrative records, semantic commitments, and habit rules.
- **Twin Engine REST API:** Constructing the FastAPI service (`main.py`) providing high-level metric summaries (`/api/overview`) and category-filtered memory queries (`/api/memories/{memory_type}`).
- **Decision Simulation & Ranking Algorithm:** Implementing vector similarity retrieval (`/api/simulate`) utilizing SciPy cosine distance to score scenario prompts against personal memories and synthesize contextual decision advice.

---

## 5-Week Progress Log & Ticket Resolutions

| Week | Date Range | Ticket / Activity Title | Log Link | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Week 1** | Aug 11 – Aug 17, 2026 | System Architecture Blueprint & The 5-Stage Adaptive Loop | [w1-ticket-resolution.md](./w1-ticket-resolution.md) | `Resolved` |
| **Week 2** | Aug 18 – Aug 24, 2026 | SQLAlchemy ORM Schema & JSON Embedding Storage in SQLite | [w2-ticket-resolution.md](./w2-ticket-resolution.md) | `Resolved` |
| **Week 3** | Aug 25 – Aug 31, 2026 | 60-Day Dataset Ingestion Engine & Episodic/Semantic Extraction | [w3-ticket-resolution.md](./w3-ticket-resolution.md) | `Resolved` |
| **Week 4** | Sep 01 – Sep 15, 2026 | FastAPI Twin Engine Core & Dynamic Overview Aggregation | [w4-ticket-resolution.md](./w4-ticket-resolution.md) | `Resolved` |
| **Week 5** | Sep 16 – Oct 13, 2026 | Vector Cosine Similarity & Decision Simulation Inference Engine | [w5-ticket-resolution.md](./w5-ticket-resolution.md) | `Resolved` |
