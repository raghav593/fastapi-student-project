from pydantic import BaseModel

class Student(BaseModel):
    roll_no:int
    name:str
    grade:int

class User(BaseModel):
    username:str
    password:str