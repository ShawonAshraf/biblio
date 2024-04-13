"""
sets up database connection and session
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def setup_db(db_url: str = "sqlite:///./test.db"):
    # check same thread is only required for sqlite
    engine = (
        create_engine(db_url)
        if "sqlite" in db_url
        else create_engine(db_url, connect_args={"check_same_thread": False})
    )

    Base = declarative_base()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return Base, SessionLocal
