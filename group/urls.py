from ast import Add
from django.urls import path
from .views import Create_Group
urlpatterns = [
    path('r1/',Create_Group ),
]