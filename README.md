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
#  Create, configure, install, initialize.
#### 🌟 Create the project directory
mkdir Todo
cd Todo

#### 🌟 Create a virtual environment (optional but recommended)
python3 -m venv env
source env/bin/activate  # On Windows, use `env\\Scripts\\activate`

#### 🌟 Install Django and Django REST framework
pip install django djangorestframework

#### 🌟 Set up a new project with a single application
django-admin startproject todo_api .
cd todo_api
django-admin startapp todo
django-admin start app user

####  🌟 Database Setup
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com

## 🌟 Models
### Todo Model

```python
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

## 🌟 Serializers

### Todo Serializer

```python
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = "__all__"

```
## 🌟 Views

### TodoList View

```python
from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TodoList(APIView):
    def get(self, request, format=None):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetails(APIView):
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```
## 🌟 URLs Base

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),
]

```
## App URLs 
```python
from .views import TodoList,TodoDetails
from django.urls import path

urlpatterns = [
   path('todos/',TodoList.as_view()),
   path('todos/<int:pk>', TodoDetails.as_view())
]
