from sqlalchemy.orm import Session
from database import models, schemas


def get_books(db: Session):
    return db.query(models.Book).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def update_book(db: Session, book_id: int, book: schemas.Book):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    db_book.book_name = book.book_name  # type: ignore
    db_book.author = book.author  # type: ignore
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    db.delete(db_book)
    db.commit()
    return db_book


def add_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(book_name=book.book_name, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
