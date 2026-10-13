# Engineering Journal — Saksham Raj

**Student Name:** Saksham Raj  
**Roll Number:** 1024030713 (Alt: 1024030710)  
**Group:** 3C52 — BE Third Year, Computer Engineering  
**Course:** Software Engineering (UCS503 / UCS503P)  
**Project:** Alter — Personal Digital Twin  
**Assigned Role:** **Full-Stack & Cloud Infrastructure Engineer**

---

## Assigned Engineering Responsibilities
- **Development Toolchain & Repository Integrity:** Normalizing cross-platform line endings (`.gitattributes`), configuring Git branching policies, and maintaining environment isolation.
- **Database Connection Management & Concurrency:** Configuring thread-safe SQLite connection parameters (`check_same_thread=False`) and lifecycle management in `database.py` via FastAPI session generators (`get_db`).
- **Python Packaging & Build Backends:** Managing modern PEP 621 packaging standards in `pyproject.toml`, resolving Hatchling build target auto-discovery failures, and ensuring deterministic package builds under `uv`.
- **Cloud Serverless Bundle Optimization:** Auditing serverless deployment footprints, diagnosing the 500MB Vercel size limit failure caused by massive PyTorch/CUDA wheels, and replacing heavy binary dependencies with lightweight alternatives.
- **Serverless Runtime Environment & File Bundling:** Resolving cloud container module path errors via `sys.path.insert` in `main.py` and configuring `vercel.json` file inclusions to bundle `alter_db.sqlite` into the serverless deployment.

---

## 5-Week Progress Log & Ticket Resolutions

| Week | Date Range | Ticket / Activity Title | Log Link | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Week 1** | Aug 11 – Aug 17, 2026 | Git Branching & Multi-OS Line-Ending Normalization | [w1-ticket-resolution.md](./w1-ticket-resolution.md) | `Resolved` |
| **Week 2** | Aug 18 – Aug 24, 2026 | SQLite Thread Concurrency & Session Lifecycle in `database.py` | [w2-ticket-resolution.md](./w2-ticket-resolution.md) | `Resolved` |
| **Week 3** | Aug 25 – Aug 31, 2026 | Resolving Hatchling Build Target & uv Sync Failures in `pyproject.toml` | [w3-ticket-resolution.md](./w3-ticket-resolution.md) | `Resolved` |
| **Week 4** | Sep 01 – Sep 15, 2026 | Overcoming Vercel 500MB Serverless Limits via Dependency Pruning | [w4-ticket-resolution.md](./w4-ticket-resolution.md) | `Resolved` |
| **Week 5** | Sep 16 – Oct 13, 2026 | Serverless SQLite Bundling & Runtime `sys.path` Resolution | [w5-ticket-resolution.md](./w5-ticket-resolution.md) | `Resolved` |
