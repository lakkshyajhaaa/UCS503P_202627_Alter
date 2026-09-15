from src.database import engine, Base
from sqlalchemy import text

def init():
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully using SQLite.")

if __name__ == "__main__":
    init()
