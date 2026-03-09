from fastapi import FastAPI
import mysql.connector as c
from pydantic import BaseModel

app = FastAPI()

conn = c.connect(host="localhost",username="root",password="admin@123",database="school")
cursor = conn.cursor()


@app.get('/')
def welcome():
    if conn.is_connected():
        return {"message":"connect succesfully"}
    else:
        return {"message":"something error come.."}
    

class Student(BaseModel):
    roll_no : int
    name : str
    grade : int


@app.get('/student')
def show_all():
    query = "select * from student"
    cursor.execute(query)
    data = cursor.fetchall()
    return data


@app.get('/student/grade')
def get_students(grade:int):
    query = "select * from student where grade=%s"
    cursor.execute(query,(grade,))
    data = cursor.fetchall()
    return data


@app.get('/student/{roll_no}')
def show_one(roll_no):
    query = "select * from student where roll_number = %s"
    cursor.execute(query,(roll_no))
    data = cursor.fetchone()
    return data


@app.post('/add-student')
def add_student(student: Student):

    query = "INSERT INTO student (roll_number,name,grade) VALUES (%s,%s,%s)"

    values = (student.roll_no, student.name, student.grade)

    cursor.execute(query, values)
    conn.commit()

    return {"message":"Student added successfully"}


@app.put("/update_student/{roll_no}")
def update_student(roll_no:int, student: Student):

    query = "UPDATE student SET name=%s, grade=%s WHERE roll_number=%s"

    cursor.execute(query,(student.name,student.grade,roll_no))
    conn.commit()

    return {"message":"Student updated"}


@app.delete("/delete-student/{roll_no}")
def delete_student(roll_no:int):

    query = "DELETE FROM student WHERE roll_number=%s"

    cursor.execute(query,(roll_no,))
    conn.commit()

    return {"message":"Student deleted"}

@app.get('/some-api')
def some_api() -> dict
    return {"mesage":"som api"}