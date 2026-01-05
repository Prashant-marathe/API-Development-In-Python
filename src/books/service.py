from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select,desc
from models import Book
from schemas import BookCreateModel, BookUpdateModel

class BookService:
    async def get_books(self, session:AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statement)
        return result.all()

    async def get_book(self, book_uid:str, session:AsyncSession):
        statement = select(Book).where(Book.uid == book_uid)
        result = await session.exec(statement)
        return result.first()

    async def create_book(self, book_data:BookCreateModel, session:AsyncSession):
        book_data_dict = book_data.model_dump()
        new_data = Book(**book_data_dict)
        session.add(new_data)
        await session.commit()
        return new_data

    async def update_book(self, book_uid:str,book_update_data:BookUpdateModel, session:AsyncSession):
        book_to_update = self.get_book(book_uid, session)
        update_book_dict = book_update_data.model_dump()
        for k, v in update_book_dict.items():
            setattr()

    async def delete_book(self, book_uid:str, session:AsyncSession):
        pass