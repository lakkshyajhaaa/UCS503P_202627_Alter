from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from pydantic import BaseModel
from typing import List, Optional
from sentence_transformers import SentenceTransformer

from src.database import get_db, engine, Base
from src.models import Memory, MemoryType

app = FastAPI(title="Alter Twin Engine API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load embedding model for the Simulate endpoint
try:
    print("Loading embedding model for API...")
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
except Exception as e:
    print(f"Warning: Failed to load sentence-transformers. Ensure it's installed. Error: {e}")
    embedding_model = None

@app.get("/api/overview")
def get_overview(db: Session = Depends(get_db)):
    """
    Returns high-level metrics for the dashboard.
    """
    total_memories = db.query(Memory).count()
    semantic_count = db.query(Memory).filter(Memory.memory_type == MemoryType.SEMANTIC).count()
    inferred_count = db.query(Memory).filter(Memory.is_inferred == True).count()
    
    # Mock some data for the UI representation
    return {
        "metrics": {
            "total_memories": total_memories,
            "prediction_accuracy": 84.2,  # Mock calculated metric
            "active_goals": 3
        },
        "semantic_insights": {
            "total_entities": semantic_count,
            "inferred_facts": inferred_count,
            "trust_score": 92
        }
    }

@app.get("/api/memories/{memory_type}")
def get_memories(memory_type: str, limit: int = 50, db: Session = Depends(get_db)):
    """
    Fetch memories by type (semantic, episodic, behavioral)
    """
    try:
        m_type = MemoryType(memory_type.lower())
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid memory type.")
        
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

class SimulationRequest(BaseModel):
    scenario: str

@app.post("/api/simulate")
def simulate_decision(request: SimulationRequest, db: Session = Depends(get_db)):
    """
    The core prediction engine.
    1. Embed the scenario.
    2. Search vector database for closest memories (pgvector cosine distance).
    3. Calculate prediction.
    """
    if not embedding_model:
        raise HTTPException(status_code=500, detail="Embedding model not loaded.")
        
    scenario_vector = embedding_model.encode(request.scenario)
    
    # Fetch all memories (In a real production app without pgvector, you'd use a vector DB like Chroma/Milvus or Faiss, 
    # but for this MVP SQLite dataset, loading them into memory is perfectly fast).
    all_memories = db.query(Memory).all()
    
    if not all_memories:
        raise HTTPException(status_code=404, detail="No memories found to simulate with.")

    # Calculate cosine similarity manually using numpy
    import numpy as np
    from scipy.spatial.distance import cosine
    
    scored_memories = []
    for m in all_memories:
        if m.embedding:
            # cosine returns distance (0 is identical). So 1 - distance = similarity.
            # But we can just sort by distance ascending (lowest distance = most relevant).
            dist = cosine(scenario_vector, m.embedding)
            scored_memories.append((dist, m))
            
    # Sort by distance (lowest first) and take top 5
    scored_memories.sort(key=lambda x: x[0])
    relevant_memories = [m[1] for m in scored_memories[:5]]
    
    # Mock prediction logic (In a real app, this goes to an LLM for final synthesis)
    prediction = "Based on your history, you are likely to decline this."
    if "travel" in request.scenario.lower() or "evening" in request.scenario.lower():
         prediction = "You typically prefer to protect your evening routine and avoid excess travel."
         
    return {
        "prediction": prediction,
        "confidence": 82,
        "reasoning": [
            {
                "content": m.content,
                "type": m.memory_type.value,
                "is_inferred": m.is_inferred
            } for m in relevant_memories
        ]
    }
