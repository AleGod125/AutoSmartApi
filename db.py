# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:1042243376@db.xessdbclpqlupdkrtvvt.supabase.co:5432/postgres"


engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"}
)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
