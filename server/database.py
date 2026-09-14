import os

from dotenv import load_dotenv
from sqlmodel import Session, create_engine

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# ตรวจสอบไม่ให้ DATABASE_URL เป็นค่าว่าง
if not DATABASE_URL:
    raise ValueError("ไม่พบค่า DATABASE_URL ในไฟล์ .env")

# สร้าง Engine สำหรับเชื่อมต่อ Supabase
engine = create_engine(DATABASE_URL, echo=True)

# Dependency Function: เปิด Session เมื่อมี Request เข้ามา และปิดอัตโนมัติเมื่อทำงานเสร็จ
def get_session():
    with Session(engine) as session:
        yield session