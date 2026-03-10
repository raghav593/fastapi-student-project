from fastapi import FastAPI
from routers import student, user
from database import conn

app = FastAPI()

app.include_router(student.router)
app.include_router(user.router)


@app.get('/')
def welcome():
    if conn.is_connected():
        return {"message":"connect succesfully"}
    else:
        return {"message":"something error come.."}
    
