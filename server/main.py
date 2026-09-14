from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from database import get_session
from models import Room

app = FastAPI(title="Meeting Room Booking API")

@app.get("/")
def health_check():
    return {"status": "online"}

@app.post("/rooms", response_model=Room)
def create_room(room: Room, session: Session = Depends(get_session)):
    session.add(room)
    session.commit()
    session.refresh(room)
    return room

@app.get("/rooms", response_model=list[Room])
def get_rooms(session: Session = Depends(get_session)):
    rooms = session.exec(select(Room)).all()
    return rooms