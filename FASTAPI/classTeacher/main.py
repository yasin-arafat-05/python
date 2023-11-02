from fastapi import FastAPI
from api import users, sections, courses
from db.model import course,user
from db.database import engine
app = FastAPI()


user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)
