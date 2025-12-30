from fastapi import FastAPI
from src.rating_engine.routes.api import router as api_router
from src.rating_engine.routes.health import router as health_router

app = FastAPI()

app.include_router(api_router)
app.include_router(health_router)

@app.get("/")
def home():
    return {"message": "Application is running!"}
