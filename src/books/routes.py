from fastapi import APIRouter, HTTPException, status, Depends
from src.books.schemas import Book, BookUpdateModel
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from src.books.service import BookService
from src.db.main import get_session

book_router = APIRouter()
book_service = BookService()
#* Get all books
@book_router.get("/", response_model=List[Book])
async def get_books(session:AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books

#* Get a single book
@book_router.get("/{book_uid}")
async def get_book(book_uid:int, session:AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.get_book(book_uid, session)
    if book:
        return book
    else:
      
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The book with id {book_uid} was not found')


#* Create a new book
@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book_data:Book, session:AsyncSession = Depends(get_session)) -> dict:
    new_book = await book_service.create_book(book_data, session)
    return new_book

#* update a book
@book_router.patch("/{book_uid}")
async def update_book(book_uid:int, book_update_data:BookUpdateModel, session:AsyncSession = Depends(get_session)) -> dict:
    updated_book = await book_service.update_book(book_uid, book_update_data, session)
    if updated_book:   
        return updated_book
    else:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The book with id {book_uid} was not found')
        
#* Deleter a Book
@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_uid:int, session:AsyncSession = Depends(get_session)):
    deleted_book = await book_service.delete_book(book_uid, session)
    if delete_book:
        return None
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The book with id {book_uid} was not found')