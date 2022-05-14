from fastapi import  FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit = 110,
          published:bool = True,
          sort: Optional[str] = None) :
    if published   :
        print("here")
        return {"data":f"this is data for only {limit}"}
    else:
        print("HEREEEE")
        return {"data":f"{limit} unpublished"}

@app.get("/blog /unpublished")
def unplublished_blog():
    return {"data":"All the unpublished blogs"}

@app.get('/about') # about PATH
def index(): # path operation function
    return {"data":"this is about page"}\

@app.get('/blog/{id}')
def show(id: int):
    return {"data":id}

################ POST request ####################

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]



@app.post('/blog')
def create_blog(blog: Blog):
    return {'data':f"BLOG IS CREATED WITH {blog.title} "}

# if __name__ == '__main__':
#     uvicorn.run(app, host = "127.0.0.1", port = 9000)