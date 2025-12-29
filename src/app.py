from fastapi import FastAPI
from src.rating_engine.routes.api import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Application is running!"}
