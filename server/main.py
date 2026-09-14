from typing import Annotated

from fastapi import Depends, FastAPI
from sqlmodel import Session, select

from database import get_session
from models import Room

app = FastAPI(title="Meeting Room Booking API")

# กำหนด Type Alias ด้วย Annotated เพื่อให้โค้ดสะอาดและไม่เกิด Warning B008
SessionDep = Annotated[Session, Depends(get_session)]

@app.get("/")
def health_check():
    return {"status": "online"}

@app.post("/rooms", response_model=Room)
def create_room(room: Room, session: SessionDep):
    session.add(room)
    session.commit()
    session.refresh(room)
    return room

@app.get("/rooms", response_model=list[Room])
def get_rooms(session: SessionDep):
    rooms = session.exec(select(Room)).all()
    return rooms