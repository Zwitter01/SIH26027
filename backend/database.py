import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Safe fallback .env reader that requires no external libraries
def _load_env_file(filepath):
    try:
        p = Path(filepath)
        if p.is_file():
            with open(p, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
    except Exception:
        pass

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent / ".env")
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
except ImportError:
    _load_env_file(Path(__file__).resolve().parent / ".env")
    _load_env_file(Path(__file__).resolve().parent.parent / ".env")

DEFAULT_PG_URL = "postgresql://postgres:admin123@localhost:5432/railwaydb"
SQLITE_PATH = os.path.abspath("railway_planner.db")

# Read DATABASE_URL from .env / environment, defaulting to local PostgreSQL railwaydb
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL", DEFAULT_PG_URL)

try:
    if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
        engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    else:
        engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
    
    # Test connection
    with engine.connect() as conn:
        print(f"[+] Connected to PostgreSQL database: {SQLALCHEMY_DATABASE_URL.split('@')[-1]}")
except Exception as e:
    print(f"[!] PostgreSQL connection failed ({e}). Falling back to local SQLite.")
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{SQLITE_PATH}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    from backend.models import Base
    Base.metadata.create_all(bind=engine)
    print("[+] Database tables verified/created successfully!")

