from pydantic import BaseModel

class User(BaseModel):
    name : str 
    email : str 
    password : str 

class Blog(BaseModel):
    title : str 
    body : str 
