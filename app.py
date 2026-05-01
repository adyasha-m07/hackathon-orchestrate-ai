from fastapi import FastAPI
from router import router

app = FastAPI(title="AI Support Ticket Router")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "API is running 🚀"}
