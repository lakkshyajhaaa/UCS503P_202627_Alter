# Week 2: SQLAlchemy ORM Schema & Embedding Storage in SQLite

## Ticket Summary
**ID:** `DB-002`  
**Assignee:** Lakkshya Jha (Lead AI Architect & Backend Systems Engineer)  
**Date:** August 21, 2026  
**Status:** Closed / Resolved  

---

## Problem / Error Description
Initial system design assumed using PostgreSQL with the `pgvector` extension for vector similarity search. However, running `pgvector` locally required external Docker containers or paid cloud managed instances, creating significant setup overhead and dependency hurdles for rapid prototype development. Furthermore, raw JSON file storage lacked ACID guarantees and indexable filters.

---

## Relevant Context
The database needs to support three distinct memory types while accommodating 384-dimensional dense vector embeddings generated from user texts, along with arbitrary JSON metadata (timestamps, energy levels, and distraction metrics).

---

## Key Observation & Root Cause Analysis
For an MVP prototype handling thousands of user memories, SQLite provides an zero-configuration embedded database. While SQLite does not natively support vector indexing extensions like HNSW out of the box, storing the raw 384-float array in a native SQLAlchemy `JSON` column allows:
1. Complete portability across any OS without binary extensions.
2. In-memory cosine distance scoring via NumPy/SciPy during query evaluation, which executes in $<15\text{ ms}$ for thousands of rows.

---

## Solution
Implemented the unified memory model in `code/src/models.py`:

```python
import uuid
import enum
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, Boolean, JSON, Enum
from src.database import Base

class MemoryType(enum.Enum):
    EPISODIC = "episodic"
    SEMANTIC = "semantic"
    BEHAVIORAL = "behavioral"

class Memory(Base):
    __tablename__ = "memories"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    memory_type = Column(Enum(MemoryType), nullable=False, index=True)
    content = Column(String, nullable=False)
    embedding = Column(JSON)  # 384-dim vector stored as JSON array
    metadata_ = Column("metadata", JSON, default={})
    is_inferred = Column(Boolean, default=False)
    confidence = Column(Float, default=1.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

---

## Because
Using SQLAlchemy with an embedded SQLite database and JSON-serialized embedding vectors achieves complete local reproducibility, eliminates external database server dependencies, and maintains a clean migration path to PostgreSQL when scale demands it.
