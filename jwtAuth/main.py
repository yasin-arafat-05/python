#--------------------------------------------------------------------------
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship,declarative_base
from pydantic import BaseModel
from typing import List
from jose import jwt
from datetime import datetime, timedelta
from jose import jwt, JWTError

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base = declarative_base()

#----------------------------------------------------Database Models---------------------

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    notes = relationship("Note", back_populates="user")

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="notes")

Base.metadata.create_all(bind=engine)

# FastAPI setup
app = FastAPI()

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


#---------------------------------------------schema model-------------------------

# User model
class UserCreate(BaseModel):
    username: str
    password: str

class UserInDB(UserCreate):
    id: int

# Note model
class NoteCreate(BaseModel):
    title: str
    content: str

class NoteInDB(NoteCreate):
    id: int

# Token model
class Token(BaseModel):
    access_token: str
    token_type: str

# OAuth2 password bearer token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# JWT Secret Key
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Function to verify user credentials
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Function to get user by username
def get_user(username: str, db):
    user = db.query(User).filter(User.username == username).first()
    return user

# Function to authenticate user and generate JWT token
def authenticate_user(db, username: str, password: str):
    user = get_user(username, db)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user

# Function to create access token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
############################################
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username
############################################
# User registration endpoint
@app.post("/register", response_model=UserInDB)
async def register(user: UserCreate):
    db = SessionLocal()
    db_user = User(username=user.username, password=pwd_context.hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user

# Token generation endpoint
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = authenticate_user(db, form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token({"sub": user.username})
    db.close()
    return {"access_token": access_token, "token_type": "bearer"}

# =--------------------------------Create a note for the authenticated user-----------------------

@app.post("/create-note", response_model=NoteInDB)
async def create_note(note: NoteCreate, current_user: str = Depends(get_current_user)):
    db = SessionLocal()
    
    print(f"Current User: {current_user}")
    
    user = get_user(current_user, db)
    if not user:
        db.close()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    db_note = Note(**note.dict(), user_id=user.id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    db.close()
    return db_note

# Fetch all notes for the authenticated user
@app.get("/user-notes", response_model=List[NoteInDB])
async def get_user_notes(current_user: str = Depends(get_current_user)):
    print(current_user)
    db = SessionLocal()
    user = get_user(current_user, db)
    if not user:
        db.close()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    notes = db.query(Note).filter(Note.user_id == user.id).all()
    db.close()
    return notes
