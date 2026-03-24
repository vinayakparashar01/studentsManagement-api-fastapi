from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json
import os

DATA_FILE = "students.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,"r") as f:
            return json.load(f)
    return []

def save_data(data):
    json_ready_data = []

    for student in data:
        if hasattr(student, "model_dump"):
            json_ready_data.append(student.model_dump())
        else:
            json_ready_data.append(student)
    with open(DATA_FILE,"w") as f:
        json.dump(json_ready_data, f, indent=4)

        
student_database = load_data()       

app = FastAPI()

# This defines what kind of data we expect to receive
class Id(BaseModel):
    name: str
    branch: str
    rollno: int
    phone: Optional[int]=None

@app.get("/")
def home():
    return {"message": "Welcome to our college api", "total_students": len(student_database)}

@app.post("/add-student")
def add_student(id: Id):
    student_database.append(id)
    save_data(student_database)
    return {"message": f"Successfully added {id.name} {id.branch}!", "data": id}

@app.get("/view-students")
def view_id():
    return student_database

@app.delete("/delete-student/{roll_no}")
def delete_student(roll_no: int):
    for student in student_database:
        if student["rollno"]== roll_no:
            student_database.remove(student)
            save_data(student_database)
            return{"message":f"student with roll no {roll_no} has been deleted"}
    return {"message": "Error:student not found"}    

@app.get("/get-student/{roll_no}")
def get_student(roll_no:int):
    for student in student_database:
        if student["rollno"]==roll_no:
            return student
    return {"message": "student not found"}    