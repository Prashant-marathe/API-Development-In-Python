from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("SERVER IS STARTING.....")
    await init_db()
    yield
    print('SERVER STOPPED....')

version="v1"

app = FastAPI(
    title="Bookly",
    description="A RestAPI for a book review web service",
    version=version,
    lifespan=lifespan,
)

app.include_router(
    book_router, 
    prefix=f"/api/{version}/books", 
    tags=['books']
)