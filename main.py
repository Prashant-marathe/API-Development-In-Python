from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    title: str
    content: str
    # optional parameter
    published: bool = True
    rating: Optional[int] = None

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my api"}

@app.get("/posts")
def get_posts():
    return {'message': 'This are all your posts'}

'''
@app.post("/createposts")
def create_posts(data:dict = Body(...)):
    print(data)
    return {"New_Post": f"Title: {data['title']} content: {data['content']}"}
'''

@app.post("/createposts")
def create_posts(post:Post):
    print(post.rating)
    #* Convert a pydantic model into dictionary 
    print(post.model_dump())
    return {f'Title':post.title,
            f'Content':post.content,
            f'Published': post.published,
            f'Rating': post.rating}
