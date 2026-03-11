from fastapi import APIRouter,Depends
from database import cursor, conn
from schemas import User
# from .student import check_login
from .auth import create_access_token


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
    user = cursor.fetchone()

    if not user:
        return {"message":"Invalid username or password"}

    token = create_access_token({"sub":user[0]})
    print(token)

    return {"access_token":token,"token_type":"bearer"}
    

# @router.get('/profile')
# def user_profile(user=Depends(check_login)):
#     return user