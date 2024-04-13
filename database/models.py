"""
models.py is used to define the database schema.
"""

from sqlalchemy import Column, Integer, String
from database.setup import setup_db

Base, SessionLocal = setup_db()


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String)
    author = Column(String)
