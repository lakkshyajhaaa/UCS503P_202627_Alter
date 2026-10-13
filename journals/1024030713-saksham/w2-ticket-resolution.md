# Week 2: SQLite Thread Concurrency & Session Lifecycle in database.py

## Ticket Summary
**ID:** `DB-002`  
**Assignee:** Saksham Raj (Full-Stack & Cloud Infrastructure Engineer)  
**Date:** August 22, 2026  
**Status:** Closed / Resolved  

---

## Problem / Error Description
During early testing of concurrent API requests on the FastAPI server, calls to database-backed endpoints crashed with SQLite threading exceptions:

```
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. 
The object was created in thread id 14032 and this is thread id 14896.
```

Furthermore, database connections were occasionally left open across asynchronous coroutines, exhausting system file handles.

---

## Relevant Context
FastAPI uses an asynchronous event loop (`asyncio`) alongside worker threadpools (`anyio`) for synchronous route handlers. SQLite enforces a strict default policy that prohibits sharing connection objects across multiple OS threads unless explicitly configured.

---

## Key Observation & Root Cause Analysis
1. SQLAlchemy's `create_engine` requires `connect_args={"check_same_thread": False}` when connecting to SQLite so that multi-threaded web servers can process requests concurrently.
2. Database sessions must not be instantiated globally; each HTTP request must obtain an isolated session and guarantee its closure via a Python generator context (`yield`).

---

## Solution
Engineered thread-safe connection pooling and dependency injection in `code/src/database.py`:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'alter_db.sqlite')
SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_path}"

# Allow multi-threaded request processing in FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Request-scoped session generator
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

Mounted `Depends(get_db)` across all FastAPI route handlers.

---

## Because
Using `check_same_thread: False` combined with FastAPI's `yield` dependency injection ensures that each incoming HTTP request operates in its own transaction context and always closes its connection, preventing deadlocks and file handle leaks.
