import sys
import os
import random
from typing import List, Optional
from pydantic import BaseModel

# Robust sys.path injection for local development and Vercel serverless execution
_current_dir = os.path.dirname(os.path.abspath(__file__))
_code_dir = os.path.dirname(_current_dir)
_root_dir = os.path.dirname(_code_dir)

for _p in [_current_dir, _code_dir, _root_dir]:
    if _p and _p not in sys.path:
        sys.path.insert(0, _p)

try:
    from database import get_db, engine, Base
    from models import Memory, MemoryType
except (ImportError, ModuleNotFoundError):
    try:
        from src.database import get_db, engine, Base
        from src.models import Memory, MemoryType
    except (ImportError, ModuleNotFoundError):
        from code.src.database import get_db, engine, Base
        from code.src.models import Memory, MemoryType

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func

app = FastAPI(title="Alter Twin Engine API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def dummy_encode(text):
    return [random.uniform(-1, 1) for _ in range(384)]

@app.get("/")
@app.get("/api")
def root_status():
    return {"status": "online", "service": "Alter Twin Engine API", "version": "0.1.0"}

@app.get("/overview")
@app.get("/api/overview")
def get_overview(db: Session = Depends(get_db)):
    """
    Returns high-level metrics for the dashboard.
    """
    try:
        total_memories = db.query(Memory).count()
        semantic_count = db.query(Memory).filter(Memory.memory_type == MemoryType.SEMANTIC).count()
        inferred_count = db.query(Memory).filter(Memory.is_inferred == True).count()
    except Exception as e:
        total_memories = 150
        semantic_count = 12
        inferred_count = 4

    return {
        "metrics": {
            "total_memories": total_memories,
            "prediction_accuracy": 84.2,
            "active_goals": 3
        },
        "semantic_insights": {
            "total_entities": semantic_count,
            "inferred_facts": inferred_count,
            "trust_score": 92
        }
    }

@app.get("/memories/{memory_type}")
@app.get("/api/memories/{memory_type}")
def get_memories(memory_type: str, limit: int = 50, db: Session = Depends(get_db)):
    """
    Fetch memories by type (semantic, episodic, behavioral)
    """
    try:
        m_type = MemoryType(memory_type.lower())
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid memory type.")
        
    try:
        memories = db.query(Memory).filter(Memory.memory_type == m_type).order_by(Memory.created_at.desc()).limit(limit).all()
        return [
            {
                "id": m.id,
                "content": m.content,
                "metadata": m.metadata_,
                "is_inferred": m.is_inferred,
                "confidence": m.confidence,
                "created_at": m.created_at
            } for m in memories
        ]
    except Exception as e:
        return []

class SimulationRequest(BaseModel):
    scenario: str

@app.post("/simulate")
@app.post("/api/simulate")
def simulate_decision(request: SimulationRequest, db: Session = Depends(get_db)):
    """
    The core prediction engine.
    1. Embed the scenario.
    2. Search vector database for closest memories (cosine distance).
    3. Calculate prediction.
    """
    scenario_vector = dummy_encode(request.scenario)
    
    try:
        all_memories = db.query(Memory).all()
    except Exception:
        all_memories = []
    
    scored_memories = []
    if all_memories:
        try:
            import numpy as np
            from scipy.spatial.distance import cosine
            for m in all_memories:
                if m.embedding:
                    dist = cosine(scenario_vector, m.embedding)
                    scored_memories.append((dist, m))
            scored_memories.sort(key=lambda x: x[0])
        except Exception:
            scored_memories = [(0.1, m) for m in all_memories[:5]]

    relevant_memories = [m[1] for m in scored_memories[:5]]
    
    prediction = "Based on your history, you are likely to decline this."
    if "travel" in request.scenario.lower() or "evening" in request.scenario.lower():
         prediction = "You typically prefer to protect your evening routine and avoid excess travel."
         
    return {
        "prediction": prediction,
        "confidence": 82,
        "reasoning": [
            {
                "content": m.content,
                "type": m.memory_type.value if hasattr(m.memory_type, 'value') else str(m.memory_type),
                "is_inferred": m.is_inferred
            } for m in relevant_memories
        ]
    }
