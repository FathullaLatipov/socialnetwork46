from fastapi import FastAPI

from posts.post_api import posts_router
from users.user_api import user_router

from starlette.staticfiles import StaticFiles

# Для запуска БД
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.mount(path='/gallery', app=StaticFiles(directory='media'))

app.include_router(user_router)
app.include_router(posts_router)