from fastapi import FastAPI,Depends,status,HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal,engine
import schemas,models,hashing


#instance of FastAPI()
app  = FastAPI()

#create all 
models.Base.metadata.create_all(bind = engine)
def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()

#____________________________________________USER PART___________________________________
#create a new user
@app.post('/createUser')
def createUser(req: schemas.User, db: Session = Depends(get_db)):
    # Check if the user with the given email already exists
    existing_user = db.query(models.User).filter(models.User.email == req.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with this email already exists.")
    
    # Create a new user
    new_user = models.User(name=req.name, email=req.email, password=hashing.Hash.bcrypt(req.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#get all the user
@app.get('/getAllUser')
def getAllUser(db:Session=Depends(get_db)):
    return db.query(models.User).all()
    
#get a user with index no.
@app.get('/singleUser/{id}')
def singleUser(id,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    return user
#update a user details
@app.put('/updateUser/{id}')
def updateUser(id,req:schemas.User,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User id {id} not found")
    user.name = req.name
    user.email = req.email
    user.password = req.password
    db.commit()
    return f"User {id} Updated"
#delete a user 
@app.delete('/deleteUser/{id}')
def deleteUser(id,db:Session=Depends(get_db)):
    get_user = db.query(models.User).filter(models.User.id==id).first()
    if not get_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    db.delete(get_user)
    db.commit()
    return f"user with id {id} deleted"
#____________________________________________BLOG PART___________________________________
#create a blog"
@app.post('/newBlog')
def newBlog(req:schemas.Blog,db: Session = Depends(get_db)):
    new_blog = models.Blog(title=req.title,body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

#get all the blog
@app.get('/getAllBlog')
def getAllBlog(db : Session = Depends(get_db)):
    return db.query(models.Blog).all()

#delete a blog
@app.delete('/delete/{id}')
def deleteABlog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    db.delete(blog)
    db.commit()
    return f"Blog with id {id} is deleted"

#update a blog
@app.put('/update/{id}')
def updateABlog(id, req: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    # Update the fields of the blog with the new values
    blog.title = req.title
    blog.body = req.body
    db.commit()
    return f"Blog with id {id} updated."