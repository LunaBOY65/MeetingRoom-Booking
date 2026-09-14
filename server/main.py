from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI
from sqlmodel import Session, select

from database import get_session
from models import Room

app = FastAPI(title="Meeting Room Booking API")

# อนุญาตให้ Next.js (port 3000) คุยกับเซิร์ฟเวอร์นี้ได้
origins = ["http://localhost:3000",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # ยอมรับทุกคำสั่ง GET, POST, PUT, DELETE
    allow_headers=["*"],
)

# กำหนด Type Alias ด้วย Annotated เพื่อให้โค้ดสะอาด
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