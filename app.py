from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Think Python", 
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-10",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id":3,
        "title": "The web socket handbook",
        "author": "Alex Diaconu",
        "publisher": "Xinyu Wang",
        "published_date": "2021-01-01",
        "page_count": 324,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Head First Javascript",
        "author": "Hellen Smith",
        "publisher": "Oreilly Media",
        "published_date": "2022-03-21",
        "page_count": 8492,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Algorithms and Data Structures in Python",
        "author": "Kent Lee",
        "publisher": "Springer, Inc",
        "published_date": "2025-11-24",
        "page_count": 4393,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Head First HTML5 Programming",
        "author": "Eric T Freemen",
        "publisher": "O'reilly Media",
        "published_date": "2024-09-14",
        "page_count": 3785,
        "language": "English"
    }
]


class Book(BaseModel):
    id:int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


#* Get all books
@app.get("/books", response_model=List[Book])
async def get_books():
    return books

#* Get a single book
@app.get("/books/{book_id}")
async def get_book(book_id:int) -> dict:
    for book in books:
        if book_id == book['id']:
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The book with id {book_id} was not found')


#* Create a new book
@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

#* update a book
@app.patch("/books/{book_id}")
async def update_book(book_id:int, book_update_data:BookUpdateModel) -> dict:
    for book in books:
        if book_id == book['id']:
            book['title'] = book_update_data.title
            book['author'] = book_update_data.author
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language
        
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The book with id {book_id} was not found')
        
#* Deleter a Book
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int):
    for book in books:
        if book_id == book['id']:
            books.remove(book)

        return {}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The book with id {book_id} was not found')