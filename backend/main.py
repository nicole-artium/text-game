from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes import game_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Text RPG API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(game_router, prefix="/api/game", tags=["game"])

@app.get("/")
def root():
    return {"message": "Text RPG API"}
