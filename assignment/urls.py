from django.urls import path
from .views import GetAllUser,GetallGroup
urlpatterns = [
    path('home/', GetAllUser),
    path('groups/', GetallGroup),
]
