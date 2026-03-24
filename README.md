# Students Management API (FastAPI)

This project is a backend REST API built using FastAPI that performs CRUD operations on student records with persistent JSON storage.

## Features

* Add student
* View all students
* Get student by roll number
* Delete student
* Data stored in JSON file
* Duplicate roll number protection

## Tech Stack

* Python
* FastAPI
* Pydantic
* JSON file storage
* Git & GitHub

## API Endpoints

POST /add-student
GET /view-students
GET /get-student/{roll_no}
DELETE /delete-student/{roll_no}

## Run Project Locally

```bash
uvicorn main:app --reload
```
