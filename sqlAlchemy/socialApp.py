from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
#
#create_engine দিয়ে ডাটাবসের সাথে python code এর connection সম্পন্ন করি।
#
from sqlalchemy.ext.declarative import declarative_base
#
#user class কে inherit করে  database এর column এর সাথে relation ঠিক রাখি । 
#
from sqlalchemy.orm import sessionmaker
#
#session create(একেক user এর জন্য একেক session) + meta data (user_name,email) 
#Data query + filtering এর কাজ গুলো করে । 
#

Base = declarative_base()

#Set Data base Path
db = "sqlite:///social.db"
engine = create_engine(db)
Base.metadata.create_all(bind = engine) 
Session = sessionmaker(bind=engine)
session = Session()

#user models
class User(Base):
    __tablename__ = "Users"
    User_id = Column("User_id",Integer,primary_key=True,index=True)
    First_Name = Column("First_Name",String)
    Last_Name = Column("Last_Name",String)
    Email = Column("Email",String)
    Profile_Name = Column("Profile_Name",String)

    def __init__(self,First_Name,Last_Name,Email,Profile_Name):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Email = Email
        self.Profile_Name = Profile_Name

#post models
class post(Base):
    __tablename__="posts"
    Post_id  = Column("Post_id",Integer,primary_key=True,index=True)
    userID = Column("userID",Integer,ForeignKey(User.User_id))
    postContent = Column("postContent",String)

    def __init__(self,userID,postContent):
        self.userID = userID
        self.postContent = postContent
        
#likes models
class likes(Base):
    __tablename__="Like"
    Like_id = Column("Like_id",Integer,primary_key=True,index=True)
    UserId = Column("UserId",Integer,ForeignKey(User.User_id))
    Post_id = Column("Post_id",Integer,ForeignKey(post.Post_id))
    def __init__(self,userID,Post_id):
        self.UserId = userID
        self.Post_id = Post_id

#add a new user Function.
def addUser(f,l,e,pn,session):
    exist = session.query(User).filter(User.Email==e).all()
    if(len(exist)>=1):
        print("User Already exist")
    else:
        USER = User(f,l,e,pn)
        session.add(USER)
        session.commit()
        print("User added to Database")

#create a new post Function 
def createPost(id,postCont):
    p = post(id,postCont)
    session.add(p)
    session.commit()
    print("A post is created")

#add like:
def addLike(userID,postID,session):
    like = likes(userID,postID)
    session.add(like)
    session.commit()
    print("Like was added")

#Output all post content
allPost = session.query(post).filter(post.userID==1).all()
allPostContent = [post.postContent for post in allPost]
print(allPostContent)

#add a exiting user will give an error
addUser("Arch","Linux","archlinux@gmail.com","Arch123",session)
#add a post
#createPost(1,"this is my first post")
#add likes to a post
addLike(1,1,session)