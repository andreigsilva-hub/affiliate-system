from fastapi import FastAPI
from database import Base, engine

from routes.users import router as users_router
from routes.offers import router as offers_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users_router)
app.include_router(offers_router)


@app.get("/")
def home():
    return {"status": "rodando"}
