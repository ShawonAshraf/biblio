"""
models.py is used to define the database schema.
"""

from sqlalchemy import Column, Integer, String
from database.db import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String)
    author = Column(String)
