from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from models import Player, Item

game_router = APIRouter()

class PlayerCreate(BaseModel):
    name: str

class PlayerResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

@game_router.post("/player", response_model=PlayerResponse)
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    existing = db.query(Player).filter(Player.name == player.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Player already exists")

    new_player = Player(name=player.name)
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player

@game_router.get("/player/{player_id}", response_model=PlayerResponse)
def get_player(player_id: int, db: Session = Depends(get_db)):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player
