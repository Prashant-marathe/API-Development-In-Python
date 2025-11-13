from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg
import time

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    # optional parameter
    published: bool = True

#* Connect to database via psycopg
while True:
    try:
        conn = psycopg.connect(host='localhost', dbname='fastapi_database', user='postgres', password='Prashant@2004', port=5432, row_factory=psycopg.rows.dict_row)
        cursor = conn.cursor()
        print('Database Connection Successful !!!')
        break
    except Exception as e:
        print(f'Error : {e}')
        time.sleep(2)

my_posts = [
{
    "title":"title of post 1",
    "content": "content of post 1",
    "id": 1
},
{
    "title": "title of post 2",
    "content": "content of post 2",
    "id" : 2
}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def root():
    return {"message": "Welcome to my api"}

@app.get("/posts")
def get_posts():
    cursor.execute('''SELECT * FROM posts''')
    posts = cursor.fetchall()
    return {'data': posts}


@app.post("/createposts", status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    cursor.execute('''
    INSERT INTO posts 
    (title, content, published) 
    VALUES
    (%s, %s, %s) RETURNING *''', (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {'data': new_post}

#* Get a single post
@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute('''SELECT * FROM posts WHERE id = %s''', (str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Error: The post with id {id} was not found.')
    return {"data": post}


#* Delete a post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    cursor.execute('''DELETE FROM posts WHERE id = %s RETURNING *''', (str(id),))
    post = cursor.fetchone()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id:{id} does not exist.')
    conn.commit()
    print(post)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#* Update a post
@app.put("/posts/{id}")
def update_post(id:int, post:Post):
    cursor.execute('''UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *''', (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not exist.')
    return {'data': updated_post}


