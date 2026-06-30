from fastapi import FastAPI

from api.routes.thumbnails import router as thumbnail_router

app = FastAPI(
    title="AutoTubeAI",
    version="1.0.0"
)

app.include_router(thumbnail_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AutoTubeAI!",
        "status": "Running"
    }