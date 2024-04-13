"""This module contains the pydantic schemas for the database models."""

from pydantic import BaseModel

# Base Book schema
# to be inherited by other schemas


class BookBase(BaseModel):
    book_name: str
    author: str


class BookCreate(BookBase):
    pass


# schema to be used by the database for
# creating a new book


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
