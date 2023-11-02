from sqlalchemy import Column,String,Integer,Table

from config.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50),nullable=False)
    email = Column(String(50),unique=True,nullable=False)
    password = Column(String(20),nullable=False)
