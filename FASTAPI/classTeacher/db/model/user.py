from sqlalchemy import Column,Integer,String,Enum,Text,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from db.model.mixins import TimeSpan
from db.database import Base
import enum

class Role(enum.Enum):
    teacher = 1
    student = 2

class User(TimeSpan, Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String(100),nullable=False,unique=True,index=True)
    role = Column(Enum(Role))
    profile = relationship("Profile",back_populates="owner",uselist=False)

class Profile(TimeSpan, Base):
    __tablename__ = "profiles"
    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String(50),nullable=False)
    last_name = Column(String(50),nullable=False)
    bio = Column(Text,nullable=True)
    is_active = Column(Boolean,default=False)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    owner = relationship("User",back_populates="profile")
