from .views import TodoList,TodoDetails
from django.urls import path

urlpatterns = [
   path('todos/',TodoList.as_view()),
   path('todos/<int:pk>', TodoDetails.as_view())
]