from fastapi import FastAPI, Depends, status, Response, HTTPException
import schemas,models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import List
#create instance 
app = FastAPI()

#creating all model into the databaes
models.Base.metadata.create_all(engine)

def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()


#-----------------------------------------------------------------------
################################Blog PART##############################
#Blog create,delete,fetch all blogs

#create post method
@app.post('/blog',status_code=status.HTTP_201_CREATED)
def creating(req :schemas.Blog, db:Session=Depends(get_db)):
    new_post = models.Blog(title=req.title,body=req.body)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

#delete a blog
@app.delete('/blog/{id}')
def deleteABlog(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    db.commit()
    return f"blog with ID NO: {id} is deleted."

#update a blog (with put method)
@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def updating(id,request:schemas.Blog,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not avaiable")
    
    blog.update({"title":f"{request.title}",
                 "body":f"{request.body}"})
    db.commit()
    return {'detail:':f"blog with id no {id} is updated"}

#get all the blog
@app.get('/allBlog',response_model=List[schemas.OutPut])
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

#get one blog at a time
@app.get('/blog/{id}',response_model=schemas.OutPut)
def getABlog(id,response:Response,db:Session=Depends(get_db)):
    fetchBlog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not fetchBlog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID NO: {id} is not available")
    return fetchBlog

#-----------------------------------------------------------------------
################################USER PART##############################
#create user, show all user, show  indivusual user.

#create a new user
@app.post('/user',status_code=status.HTTP_201_CREATED)
def createUser(req:schemas.User, db : Session = Depends(get_db)):
    new_user = models.User(name=req.name,email=req.email,password=req.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# #show all user
# @app.get('/showAllUser')
# def showAllUser(db:Session=Depends(get_db)):
#     getUser = db.query(models.User).all()
#     return getUser

# #show a single user
# @app.get('/showASingleUser')
# def showASingleUser(id,db:Session=Depends(get_db)):
#     res = db.query(models.User).filter(models.User.id==id).first()
#     if not res:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User id {id} is not found")
#     return res
