import os
from dotenv import load_dotenv
from sqlmodel import create_engine, Session

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# สร้าง Engine สำหรับเชื่อมต่อ Supabase
engine = create_engine(DATABASE_URL, echo=True)

# Dependency Function: เปิด Session เมื่อมี Request เข้ามา และปิดอัตโนมัติเมื่อทำงานเสร็จ
def get_session():
    with Session(engine) as session:
        yield session