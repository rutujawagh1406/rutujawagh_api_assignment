import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ Get the database URL
DATABASE_URL = os.getenv("DATABASE_URL")
print("DB URL:", DATABASE_URL)  # For debugging

# ✅ Initialize SQLAlchemy engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
