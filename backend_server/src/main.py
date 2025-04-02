from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import connect_db
from model import Member
from typing import List
import uvicorn


app = FastAPI()

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả các origin trong môi trường development
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép tất cả các HTTP methods
    allow_headers=["*"],  # Cho phép tất cả các headers
)


@app.get("/")
def home():
    return{"message": "hello world"}


# API thêm thành viên
@app.post("/add_member/")
def add_member(member: Member):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO members (fullname, birthdate, hometown) VALUES (?, ?, ?)", 
                   (member.fullname, member.birthdate, member.hometown))
    conn.commit()
    conn.close()
    return {"message": "Thêm thành viên thành công"}


# API lấy danh sách thành viên
@app.get("/get_members/", response_model=List[Member])
def get_members():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT fullname, birthdate, hometown FROM members")
    members = [Member(fullname=row[0], birthdate=row[1], hometown=row[2]) for row in cursor.fetchall()]
    conn.close()
    return members


# API tìm kiếm theo tên
@app.get("/search_member/{name}")
def search_member(name: str):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT fullname, birthdate, hometown FROM members WHERE fullname LIKE ?", ('%' + name + '%',))
    result = cursor.fetchall()
    conn.close()
    if not result:
        raise HTTPException(status_code=404, detail="Không tìm thấy thành viên")
    return [{"fullname": row[0], "birthdate": row[1], "hometown": row[2]} for row in result]


# API tìm kiếm theo quê quán
@app.get("/search_hometown/{hometown}")
def search_hometown(hometown: str):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT fullname, birthdate, hometown FROM members WHERE hometown LIKE ?", ('%' + hometown + '%',))
    result = cursor.fetchall()
    conn.close()
    return [{"fullname": row[0], "birthdate": row[1], "hometown": row[2]} for row in result]


# API sắp xếp theo tuổi
@app.get("/sort_by_age/")
def sort_by_age():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT fullname, birthdate, hometown FROM members ORDER BY birthdate ASC")
    result = cursor.fetchall()
    conn.close()
    return [{"fullname": row[0], "birthdate": row[1], "hometown": row[2]} for row in result]


# API reset database
@app.delete("/reset_database/")
def reset_database():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM members")  # Xóa toàn bộ dữ liệu
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='members'")  # Reset ID (nếu có)
    conn.commit()
    conn.close()
    return {"message": "Database đã được reset thành công"}


if __name__ == "__main__":
        uvicorn.run("main:app", host="0.0.0.0", port=3001, reload=True)
