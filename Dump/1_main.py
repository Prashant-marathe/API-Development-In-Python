# from fastapi import FastAPI, Header
# from typing import Optional
# from pydantic import BaseModel


# app = FastAPI()

# @app.get("/")
# async def read_root():
#     return {'message': 'Hello World'}

# @app.get("/greet")
# async def get_user(name:Optional[str] = 'User', age:int = 0) -> dict:
#     return {'message': f'Hello {name}', 'age':age}

# class Book(BaseModel):
#     title:str
#     author:str


# @app.post("/create_book")
# async def create_book(book:Book):
#     return {'message': book}

# @app.get("/get_headers", status_code=200)
# async def get_headers(
#     accept:str = Header(None),
#     host:str = Header(None),
#     content_type = Header(None),
#     user_agent = Header(None)
# ):
#     request_headers = {}

#     request_headers['Accept'] = accept
#     request_headers['Content-Type'] = content_type
#     request_headers['User-Agent'] = user_agent
#     request_headers['Host'] = host

#     return request_headers 

