from fastapi import APIRouter,Depends
from database import cursor, conn
from schemas import User
from .student import check_login

router = APIRouter()

@router.post("/register")
def register(user:User):

    query = "INSERT INTO users (username,password) VALUES (%s,%s)"
    cursor.execute(query,(user.username,user.password))
    conn.commit()

    return {"message":"User registered"}


@router.post("/login")
def login(user:User):

    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query,(user.username,user.password))

    data = cursor.fetchone()

    if data:
        return {"message":"Login successful"}
    else:
        return {"message":"Invalid username or password"}
    

@router.get('/profile')
def user_profile(user=Depends(check_login)):
    return user