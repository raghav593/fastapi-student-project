from fastapi import APIRouter,Depends
from database import cursor, conn
from schemas import Student
from fastapi import HTTPException

router = APIRouter()

def check_login(username:str, password:str):

    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query,(username,password))

    user = cursor.fetchone()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    return user


@router.get('/student')
def show_all(user=Depends(check_login)):
    query = "select * from student"
    cursor.execute(query)
    return cursor.fetchall()


@router.get('/student/grade')
def get_students(grade:int,user=Depends(check_login)):

    query = "select * from student where grade=%s"
    cursor.execute(query,(grade,))
    return cursor.fetchall()


@router.get('/student/{roll_no}')
def show_one(roll_no:int,user=Depends(check_login)):

    query = "select * from student where roll_number=%s"
    cursor.execute(query,(roll_no,))
    return cursor.fetchone()


@router.post('/add-student')
def add_student(student:Student,user=Depends(check_login)):

    query = "INSERT INTO student (roll_number,name,grade) VALUES (%s,%s,%s)"
    cursor.execute(query,(student.roll_no,student.name,student.grade))
    conn.commit()

    return {"message":"Student added successfully"}


@router.put("/update-student/{roll_no}")
def update_student(roll_no:int,student:Student,user=Depends(check_login)):

    query = "UPDATE student SET name=%s, grade=%s WHERE roll_number=%s"
    cursor.execute(query,(student.name,student.grade,roll_no))
    conn.commit()

    return {"message":"Student updated"}


@router.delete("/delete-student/{roll_no}")
def delete_student(roll_no:int,user=Depends(check_login)):

    query = "DELETE FROM student WHERE roll_number=%s"
    cursor.execute(query,(roll_no,))
    conn.commit()

    return {"message":"Student deleted"}


