# Notes API 

A simple and clean RESTful Notes API built with FastAPI and SQLAlchemy.

This project demonstrates a basic backend architecture, CRUD operations, database interaction using ORM, and modern API development practices.

# Features

Create notes

Retrieve all notes

Retrieve a note by ID

Update notes partially (PATCH)

Delete notes

SQLite database with SQLAlchemy ORM

Automatic API documentation (Swagger / OpenAPI)

# Tech Stack

Python 3.10+

FastAPI

SQLAlchemy 2.0

SQLite

Pydantic

Uvicorn

# Data Model
Task 
Field	Type	Description 
id	int	Primary key 
title	str	Note title 
description	str	Optional note description 
done	bool	Completion status 
created_at	datetime	Creation timestamp (UTC) 
# API Endpoints
Create a note

POST /notes/

{
  "title": "My first note",
  "description": "Some text"
}

Get all notes

GET /notes/

Get note by ID

GET /notes/{id}

Update a note (partial)

PATCH /notes/{id}

{
  "title": "Updated title",
  "done": true
}

Delete a note

DELETE /notes/{id}

# Getting Started
1. Clone the repository
git clone https://github.com/your-username/notes-api.git
cd notes-api

2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows

3. Install dependencies
pip install fastapi uvicorn sqlalchemy

4. Run the application
uvicorn Notes_API.app.main:app --reload

# API Documentation

After starting the server, open:

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc
