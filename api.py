from fastapi import FastAPI
from schemas.book import Book, BookWithId

app = FastAPI()

@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "biblio api is running!"
    }

@app.get("/books")
async def get_books():
    return {
        "status": "ok",
        "books": []
    }
    
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    return {
        "book": {},
    }
    
@app.post("/books/add")
async def add_book(book: Book):
    return {
        "book": {},
    }
    
@app.put("/books/update/{book_id}")
async def update_book(book_id: int):
    return {
        "book": {},
    }
    
@app.delete("/books/delete/{book_id}")
async def delete_book(book_id: int):
    return {
        "book": {},
    }
