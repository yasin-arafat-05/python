from fastapi import FastAPI
from config.db import engine
from models import user
import routes
app = FastAPI()

user.Base.metadata.create_all(bind=engine)

app.include_router(routes.user.router)