# Todo List API

A Django REST API for managing a todo list.

# Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Authentication](#authentication)
7. [Examples](#examples)
8. [Testing](#testing)
9. [Contributing](#contributing)
10. [License](#license)
11. [Manual Installation Process](#installation)

# Introduction

Todo List API is a Django-powered REST API designed to facilitate the management of todo tasks. It provides a set of endpoints for creating, updating, deleting, and fetching todo items.

# Features

- User authentication for secure access
- CRUD operations for todo items
- ...

# Installation
To get started with the Todo List API, follow these installation steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/todo-list-api.git

# Change into the project directory
cd todo-list-api

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate
```
#  Inital Installation and setup process....
## 🌟 Create the project directory
mkdir Todo
cd Todo

## 🌟 Create a virtual environment (optional but recommended)
python3 -m venv env
source env/bin/activate  # On Windows, use `env\\Scripts\\activate`

## 🌟 Install Django and Django REST framework
pip install django djangorestframework

## 🌟 Set up a new project with a single application
django-admin startproject todo_api .
cd todo_api
django-admin startapp todo
django-admin start app user

##  🌟 Database Setup
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com

## 🌟 Models
from django.db import models
class Todo(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title




