from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router   # ✅ CORRECT IMPORT
print("MAIN FILE LOADED")
app = FastAPI()

# ✅ Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
