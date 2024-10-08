﻿# Task Manager Project

A task management web application built using Django, Celery, and WebSockets. This project handles background tasks asynchronously and supports real-time updates using WebSockets.

## Features
- Task creation, updates, and deletion.
- Real-time updates using WebSockets.
- Background task processing using Celery and Redis.
- Pagination for task listing.

## Prerequisites

Make sure you have the following software installed:
- Python 3.10+
- Virtualenv
- Django 5.1.1
- Celery
- Daphne (for handling ASGI/WebSockets)
- Redis (for Celery message broker and backend)
- PostgreSQL or SQLite (for database)

## Installation

Follow the steps below to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone <your-repository-url>

```


### 2. Set Up a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Linux/Mac)
source venv/bin/activate

# Activate virtual environment (Windows)
venv\Scripts\activate
```



### 3. Install Dependencies
Use the requirements.txt file to install all the required packages:
```bash
# Create virtual environment
pip install -r requirements.txt

```


### 4. Apply Database Migrations
To create the necessary tables in the database, run:
```bash
python manage.py migrate

```


### 5. Create a Superuser
To access the Django admin panel, create a superuser:
```bash
python manage.py createsuperuser


```


### 6. Create a Superuser
Running the Application
```bash
python manage.py runserver

```



### 7. Start Daphne (ASGI Server)
Daphne is required for handling WebSocket connections. Run it on port 8001:
```bash
daphne -p 8001 task_project.asgi:application


```




### 8. Start Celery Worker
Celery is used for handling background tasks asynchronously. Start a Celery worker:
```bash
celery -A task_project worker --loglevel=debug


```

