from typing import Optional
import uuid
from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class Room(SQLModel, table=True):
    __tablename__: str = "rooms"

    # ใช้ default_factory เพื่อให้ Python สร้าง UUID4 ทันทีเมื่อมีการสร้าง Instance
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4, 
        primary_key=True
    )
    name: str
    capacity: int
    building: str
    floor: str
    requires_approval: bool = False
    is_active: bool = True
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )