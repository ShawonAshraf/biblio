"""
sets up database connection and session
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

DB_URL = os.getenv("DB_URL", "sqlite:///./biblio.db")

engine = (
    create_engine(DB_URL)
    if "sqlite" in DB_URL
    else create_engine(DB_URL, connect_args={"check_same_thread": False})
)

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
