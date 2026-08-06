# AI SQL Assistant - Backend Documentation

## Project Overview

**AI SQL Assistant** is an AI-powered SQL learning platform that allows users to upload CSV or Excel datasets, automatically converts them into a SQLite database, executes SQL queries, detects SQL errors, provides AI-generated corrections, and generates SQL practice questions with solutions.

The goal of this project is to help beginners learn SQL interactively using Artificial Intelligence.

---

# Features

## 1. Dataset Upload

* Upload CSV files
* Upload Excel (.xlsx/.xls) files
* Validate uploaded files
* Automatically create SQLite tables
* Replace existing tables when uploading the same file again

---

## 2. SQL Query Execution

* Execute SQL SELECT queries
* Display query results
* Display column names
* Display total number of rows
* Return SQL execution errors

---

## 3. SQL Safety

Dangerous SQL commands are blocked.

Blocked Commands:

* DROP
* DELETE
* UPDATE
* INSERT
* ALTER
* CREATE
* TRUNCATE

---

## 4. AI SQL Error Assistant

If the SQL query contains errors:

* Detect SQL syntax errors
* Explain the mistake
* Generate the corrected SQL query
* Provide beginner-friendly explanation
* Suggest improvements

Example:

User Query

SELEC * FROM employee;

↓

SQLite Error

↓

Groq AI

↓

Correct Query

SELECT * FROM employee;

---

## 5. Dynamic Schema Detection

The application automatically detects:

* Table Name
* Column Names

Example

employee.csv

↓

SQLite Table

employee

↓

Schema

employee(employee_id, name, department, salary)

No hardcoded schema is used.

---

## 6. AI SQL Learning Generator

Based on uploaded dataset:

Generate

* Easy SQL Questions
* Medium SQL Questions
* Hard SQL Questions

For every question AI provides

* Question
* SQL Query
* Explanation

---

# Technology Stack

Backend

* Python
* FastAPI

Database

* SQLite

Data Processing

* Pandas
* SQLAlchemy

Artificial Intelligence

* Groq API
* Llama 3.3 70B Versatile

Environment

* python-dotenv

---

# Project Structure

backend/

├── app.py

├── requirements.txt

├── .env

├── database/

│ └── database.db

├── uploads/

├── prompts/

│ ├── sql_error_prompt.txt

│ └── sql_learning_prompt.txt

├── routes/

│ ├── upload.py

│ ├── query.py

│ └── learning.py

├── services/

│ ├── file_service.py

│ ├── sql_service.py

│ |── ai_service.py

| └── csv_service.py

---
# Folder Explanation
database/database.db

stores the SQLite database

prompts/
sql_error_prompt.txt
sql_learning_prompt.txt

contains all AI prompt templates

routes/
upload.py

Handles,
POST /upload
Responsibilities:
Receive uploaded file
Save file
Call csv_service.py

query.py

Handles,
POST /query
Responsibilities:
Receive SQL query
Call sql_service.py
Return results

learning.py

Handles,
POST /learning
Responsibilities:
Receive table name
Call AI
Return SQL practice questions

services/
csv_service.py 

Responsible for:

Reading CSV/Excel files
Converting them to Pandas DataFrame
Saving the DataFrame into SQLite
Returning dataset information

file_service.py

Responsible for:

File validation
File type checking
File extension checking

sql_service.py

Responsible for:

Execute SQL
Validate SQL
Block dangerous queries
Detect schema
Call AI if SQL fails

Everything related to SQL belongs here.

ai_service.py

Purpose

Load prompts
Connect to Groq
Analyze SQL errors
Generate learning questions

only AI-related code should be here

uploads/ 
whenever user uploads file, it stored here
after reads, the data is stored in SQLite

.env
contains,
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx
no spaces should there

backend/app.py
This is the starting point of FastAPI.
Think of it as the main controller.
Responsibilities:
Create FastAPI app
Register routes
Start server
---
# Architecture
                 User

                   │

                   ▼

             FastAPI (app.py)

                   │

     ┌─────────────┼─────────────┐

     ▼             ▼             ▼

 upload.py     query.py     learning.py

     │             │             │

     ▼             ▼             ▼

csv_service   sql_service   ai_service

     │             │             │

     ▼             ▼             ▼

 SQLite      Execute SQL      Groq AI

     │             │             │

     └─────────────┼─────────────┘

                   ▼

              JSON Response
---
# Installation

## Step 1

Create Project Folder "AI SQL ASSISTANT"

ADD backend folder

cd backend

---

## Step 2

Create Virtual Environment

Windows

python -m venv venv

Activate

venv\Scripts\activate

---

## Step 3

Install Dependencies

pip install -r requirements.txt

---

## Step 4

Create .env

Example

GROQ_API_KEY=your_groq_api_key

---

## Step 5

Run FastAPI

uvicorn app:app --reload

Swagger

http://127.0.0.1:8000/docs

---

# API Documentation

## API 1

POST /upload

Purpose

Upload CSV or Excel file.

Request

Multipart Form Data

file

Response

{
"table":"employee",
"rows":100,
"columns":[
"employee_id",
"name",
"department",
"salary"
]
}

---

## API 2

POST /query

Purpose

Execute SQL query.

Request

{
"query":"SELECT * FROM employee"
}

Success Response

{
"success":true,
"columns":[...],
"total_rows":100,
"rows":[...]
}

Error Response

{
"success":false,
"database_error":"SQL Error",
"ai_feedback":{
"mistake":"",
"correct_query":"",
"explanation":"",
"suggestion":""
}
}

---

## API 3

POST /learning

Purpose

Generate SQL learning content.

Request

{
"table_name":"employee"
}

Response

{
"success":true,
"learning":{
"easy":[...],
"medium":[...],
"hard":[...]
}
}

---

# Backend Workflow

## Module 1

Project Setup

↓

FastAPI

↓

SQLite

↓

Folder Structure

---

## Module 2

Upload Dataset

↓

CSV / Excel

↓

Pandas

↓

SQLite Table

---

## Module 3

SQL Execution

↓

User SQL

↓

SQLite

↓

Result

---

## Module 4

AI SQL Error Correction

↓

Wrong SQL

↓

SQLite Error

↓

Groq AI

↓

Correction

↓

Suggestion

---

## Module 5

Dynamic Schema Detection

↓

Read Table Name

↓

Read SQLite Schema

↓

Pass Schema to AI

---

## Module 6

AI Learning Generator

↓

Read Schema

↓

Groq AI

↓

Easy Questions

↓

Medium Questions

↓

Hard Questions

↓

SQL Solutions

↓

Explanation

---

# Prompt Engineering

The prompts are stored separately inside the prompts folder.

Advantages

* Easy to maintain
* Easy to update
* Separation of business logic and prompts

Current Prompt Files

sql_error_prompt.txt

Purpose

Detect SQL errors and generate corrections.

sql_learning_prompt.txt

Purpose

Generate SQL practice questions and SQL solutions.

---

# Error Handling

Application handles

* Invalid file format
* Empty SQL query
* SQL syntax errors
* Missing tables
* Unsupported SQL commands
* AI response parsing errors

---


# Learning Outcomes

Through this project the following concepts are implemented:

* FastAPI REST APIs
* File Upload Handling
* SQLite Database Integration
* SQL Query Execution
* SQL Validation
* Prompt Engineering
* Groq API Integration
* AI-powered Error Analysis
* Dynamic Schema Detection
* AI-generated SQL Learning Content
* Modular Backend Architecture

---
