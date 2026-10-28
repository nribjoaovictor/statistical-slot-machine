from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Statistical Slot Machine API",
        "status": "running"
    }