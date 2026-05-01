from fastapi import FastAPI
from router import router

app = FastAPI(
    title="Hackathon Orchestrate AI",
    description="AI-powered ticket routing system for HackerRank, Claude, and Visa",
    version="1.0.0"
)

app.include_router(router)
