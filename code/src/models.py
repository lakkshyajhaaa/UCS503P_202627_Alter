import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, Integer, DateTime, Boolean, JSON, Enum
from src.database import Base
import enum

class MemoryType(enum.Enum):
    EPISODIC = "episodic"
    SEMANTIC = "semantic"
    BEHAVIORAL = "behavioral"

class Memory(Base):
    """
    Unified memory model for all three layers.
    """
    __tablename__ = "memories"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    memory_type = Column(Enum(MemoryType), nullable=False)
    
    # Core content for semantic search
    content = Column(String, nullable=False)
    
    # Store embedding as JSON since we dropped pgvector for SQLite compatibility
    embedding = Column(JSON)
    
    # Optional metadata (JSON) to store specific fields like date, duration, category, confidence
    metadata_ = Column("metadata", JSON, default={})
    
    # Trust layer
    is_inferred = Column(Boolean, default=False)
    confidence = Column(Float, default=1.0)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
