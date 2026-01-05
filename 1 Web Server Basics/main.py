from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root() -> dict:
    return {"message": "We are reading root"}

# & Path Parameters
@app.get("/home/{name}")
def greet_user(name:str = "User") -> dict:
    return {"message": f"Hello, {name}"}

# ^ Query Parameters
@app.get("/user/{name}")
def get_user_info(name:str = "User", age:int = None) -> dict:
    return {"message":f"name: {name} and age: {age}"}

# * Optional Parameters
@app.get("/Optional")
def optional(name:Optional[str] = "user", age:int = 21):
    return {"message": f'name: {name} and age: {age}'}