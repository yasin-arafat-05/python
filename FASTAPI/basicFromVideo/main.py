from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
#create instance of FastAPI
app = FastAPI()

@app.get('/')
def home():
    return "This is home page"

#create dynamic route
@app.get('/about/{id}/{name}')
def about(id:int, name:str):
    return {"Owner":"Yasin Aafat",
            "id":id,
            "comment":name}

#query parameter
@app.get('/blog')
def blogList(limit:int = 5,published:bool = True,sort:Optional[str] = None):
    if published:
        return f"{limit} blog published {sort}"
    else:
        return f"all the blog published {sort}"
    
#_______________________________________________
#request body (app.post())
#post method is available in sweagger UI

#inherite base model class
class CreateBlog(BaseModel):
    title:str
    body:str
    published: Optional[bool]

#post path
@app.post('/post')
def newBlog(req :CreateBlog):
    return f"blog is created with {req.title}"
