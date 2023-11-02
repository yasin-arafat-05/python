from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from fastapi import Depends
DATABASEURL = "mysql+pymysql://root:b5555@localhost:3306/BlogApplication"

engine = create_engine(DATABASEURL)

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()

#db utillite
def db_get():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()


