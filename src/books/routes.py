from fastapi import APIRouter, HTTPException, status
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel
from typing import List

book_router = APIRouter()

#* Get all books
@book_router.get("/", response_model=List[Book])
async def get_books():
    return books

#* Get a single book
@book_router.get("/{book_id}")
async def get_book(book_id:int) -> dict:
    for book in books:
        if book_id == book['id']:
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The book with id {book_id} was not found')


#* Create a new book
@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

#* update a book
@book_router.patch("/{book_id}")
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
@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int):
    for book in books:
        if book_id == book['id']:
            books.remove(book)

        return {}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The book with id {book_id} was not found')