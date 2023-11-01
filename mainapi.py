from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# endpoints: aws.com/delete-user
# GET,POST,PUT,DELETE
students = {
    1: {
        'name':'John',
        'age':17,
        'year': 'year 12'
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: str
    age: int
    year: str
    
@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student_data(student_id: int = Path(description="The ID of the student you want to view", gt=0,lt=3)):
    return students[student_id]

# gt, lt, ge, le

@app.get("/get-by-name/{student_id_}")
def get_student_data(*,student_id_: int, name: Optional[str] = None, test :int):
    for student_id_ in students:
        if students[student_id_]["name"] == name:
            return students[student_id_]
    return {"Data": "Not found"}

@app.post("/create-student/{student-id}")
def create_student(student_id:int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    
    students[student_id] = student 
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    
    del students[student_id]
    return {"Message":f"Success deleted student {student_id}"}