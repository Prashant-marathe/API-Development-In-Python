from fastapi import APIRouter, status, HTTPException
from typing import List
from src.books.books_data import books
from src.books.schemas import DataBook, BookUpdateModel

book_router = APIRouter()

#* Get books
@book_router.get("/", response_model = List[DataBook])
async def get_books():
    return books

#* Create a new book
@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book_data:DataBook) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

#* Get a single book
@book_router.get("/{book_id}")
async def get_book(book_id:int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The id {book_id} not found.')

#* Update an book
@book_router.patch("/{book_id}")
async def update_book(book_id:int, book_update_data:BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['author'] = book_update_data.author
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language

            return {'message': "book updated successfully"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The book with id {book_id} not found.')


#* Delete an book
@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The book with id {book_id} not found.')