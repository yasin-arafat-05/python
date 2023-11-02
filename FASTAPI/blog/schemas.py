from pydantic import BaseModel

class Blog(BaseModel):
    title : str 
    body  : str


#Response Model -> To give Output;
class OutPut(BaseModel):
    title : str
 

 #Base model create-> class ->(models.py-> database's model)
class User(BaseModel):
    name : str
    email : str 
    password : str 
