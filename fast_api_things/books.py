from fastapi import FastAPI

app = FastAPI()

# to run app use the command: uvicorn books:app --reload

BOOKS = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}, 
    {"id": 4, "title": "Brave New World", "author": "Aldous Huxley"},
    {"id": 5, "title":  "The Catcher in the Rye", "author": "J.D. Salinger"}]

@app.get("/")
async def root():
    """
    Root endpoint
    """
    return {"message": "Welcome to the Book API!"}

@app.get("/api-endpoint/books")
async def get_books():
    """
    Get all books
    """
    return BOOKS
@app.get("/api-endpoint/books/{book_id}")
async def get_book(book_id: int):
    """
    Get a book by ID
    """
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}
@app.post("/api-endpoint/books")
async def create_book(book: dict):
    """
    Create a new book
    """
    book["id"] = len(BOOKS) + 1
    BOOKS.append(book)
    return book
@app.put("/api-endpoint/books/{book_id}")
async def update_book(book_id: int, book: dict):
    """
    Update a book by ID
    """
    for index, b in enumerate(BOOKS):
        if b["id"] == book_id:
            BOOKS[index].update(book)
            return BOOKS[index]
    return {"error": "Book not found"}
@app.delete("/api-endpoint/books/{book_id}")
async def delete_book(book_id: int):
    """
    Delete a book by ID
    """
    for index, book in enumerate(BOOKS):
        if book["id"] == book_id:
            del BOOKS[index]
            return {"message": "Book deleted"}
    return {"error": "Book not found"}