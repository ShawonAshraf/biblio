from fastapi import FastAPI, Depends, HTTPException

from sqlalchemy.orm import Session


from database import crud, schemas
from database.db import SessionLocal

from loguru import logger


app = FastAPI()


# Dependency
# gives a database context to the api
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"status": "ok", "message": "biblio api is running!"}


@app.get("/books", response_model=list[schemas.Book])
async def get_books(db: Session = Depends(get_db)):
    try:
        db_books = crud.get_books(db)
        return db_books
    except Exception as e:
        logger.error(f"Error: {e}")
        return []


@app.get("/books/{book_id}", response_model=schemas.Book)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    try:
        book = crud.get_book_by_id(db, book_id)
        return book
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=404, detail="Book not found!")


@app.post("/books/add", response_model=schemas.Book)
async def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    new_book = crud.add_book(db, book)
    if not new_book:
        logger.error("Book already exists!")
        raise HTTPException(status_code=201, detail="Book already exists!")
    return new_book


@app.put("/books/update/{book_id}", response_model=schemas.Book)
async def update_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if not book:
        logger.error("Book not found!")
        raise HTTPException(status_code=404, detail="Book not found!")
    return crud.update_book(db, book_id, book)


@app.delete("/books/delete/{book_id}", response_model=schemas.Book)
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if not book:
        logger.error("Book not found!")
        raise HTTPException(status_code=404, detail="Book not found!")
    return crud.delete_book(db, book_id)
