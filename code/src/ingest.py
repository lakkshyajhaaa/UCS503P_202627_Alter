import pandas as pd
import random
import os
from src.database import SessionLocal
from src.models import Memory, MemoryType

# Fallback: Generate a random 384-dimensional vector for local MVP testing
# This avoids PyTorch dependency hell on the local machine
def dummy_encode(texts):
    return [[random.uniform(-1, 1) for _ in range(384)] for _ in texts]

def ingest_data():
    db = SessionLocal()
    
    # Clear existing data
    db.query(Memory).delete()
    db.commit()
    print("Cleared existing memories.")

    # Load dataset
    csv_path = os.path.join(os.path.dirname(__file__), '..', '..', 'dataset', 'continuous_60_day_ai_schedule_dataset.csv')
    df = pd.read_csv(csv_path)
    
    memories_to_add = []

    print(f"Processing {len(df)} rows from dataset...")
    
    # 1. Episodic Memories (Sample 100 rows to keep it fast, or process all if small enough)
    for _, row in df.iterrows():
        # Create a narrative sentence
        completed = "completed" if row['task_completed'] == 1 else "did not complete"
        content = f"On {row['date']} ({row['day_of_week']}) from {row['time_start']} to {row['time_end']}, I {completed} '{row['activity']}' ({row['category']})."
        
        metadata = {
            "date": row['date'],
            "day_of_week": row['day_of_week'],
            "category": row['category'],
            "duration": row['duration_min'],
            "energy_level": row['energy_level_1_5'],
            "distraction_level": row['distraction_level']
        }
        
        memories_to_add.append({
            "memory_type": MemoryType.EPISODIC,
            "content": content,
            "metadata_": metadata,
            "is_inferred": False,
            "confidence": 1.0
        })

    # 2. Semantic Memories (Extracting facts)
    # E.g., What are the fixed schedule activities?
    fixed_activities = df[df['is_fixed_schedule'] == 1]['activity'].unique()
    for activity in fixed_activities:
        memories_to_add.append({
            "memory_type": MemoryType.SEMANTIC,
            "content": f"My schedule requires mandatory fixed time for: {activity}.",
            "metadata_": {"category": "Fixed Commitment"},
            "is_inferred": False,
            "confidence": 1.0
        })

    # 3. Behavioral Memories (Extracting patterns)
    # E.g., Average completion rate when distraction is high vs low
    if 'distraction_level' in df.columns:
        high_distraction = df[df['distraction_level'] == 'High']
        if not high_distraction.empty:
            completion_rate = high_distraction['task_completed'].mean() * 100
            memories_to_add.append({
                "memory_type": MemoryType.BEHAVIORAL,
                "content": f"When my distraction level is High, my task completion rate drops to {completion_rate:.1f}%.",
                "metadata_": {"insight_type": "Distraction Impact"},
                "is_inferred": True,
                "confidence": 0.85
            })

    # Batch process embeddings and save
    print(f"Generating embeddings for {len(memories_to_add)} memories...")
    
    batch_size = 64
    for i in range(0, len(memories_to_add), batch_size):
        batch = memories_to_add[i:i+batch_size]
        contents = [m['content'] for m in batch]
        
        # Generate embeddings
        embeddings = dummy_encode(contents)
        
        for j, memory_data in enumerate(batch):
            mem = Memory(
                memory_type=memory_data['memory_type'],
                content=memory_data['content'],
                embedding=embeddings[j],
                metadata_=memory_data['metadata_'],
                is_inferred=memory_data['is_inferred'],
                confidence=memory_data['confidence']
            )
            db.add(mem)
        
        db.commit()
        print(f"Inserted batch {i//batch_size + 1}")

    db.close()
    print("Ingestion complete!")

if __name__ == "__main__":
    ingest_data()
