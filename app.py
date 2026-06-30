from fastapi import FastAPI

app = FastAPI(
    title="AutoTubeAI",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AutoTubeAI!",
        "status": "Running"
    }