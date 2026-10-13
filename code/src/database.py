from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

candidate_paths = [
    os.path.join(BASE_DIR, 'alter_db.sqlite'),
    os.path.join(os.getcwd(), 'code', 'src', 'alter_db.sqlite'),
    os.path.join(os.getcwd(), 'alter_db.sqlite'),
    '/tmp/alter_db.sqlite',
]

source_db = None
for p in candidate_paths:
    if os.path.exists(p) and os.path.getsize(p) > 0:
        source_db = p
        break

# On Vercel / AWS Lambda, /var/task is read-only; copy to /tmp for safe SQLite locking
is_serverless = bool(os.environ.get("VERCEL") or os.environ.get("AWS_LAMBDA_FUNCTION_NAME") or not os.access(BASE_DIR, os.W_OK))

if is_serverless:
    target_db = '/tmp/alter_db.sqlite'
    if source_db and source_db != target_db:
        if not os.path.exists(target_db) or os.path.getsize(target_db) == 0:
            try:
                shutil.copyfile(source_db, target_db)
            except Exception as e:
                print(f"Warning copying DB to /tmp: {e}")
    db_path = target_db if os.path.exists(target_db) else (source_db or os.path.join(BASE_DIR, 'alter_db.sqlite'))
else:
    db_path = source_db if source_db else os.path.join(BASE_DIR, 'alter_db.sqlite')

SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
