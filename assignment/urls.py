from django.urls import path
from .views import GetAllUser,GetallGroup,PostAssignment
urlpatterns = [
    path('home/', GetAllUser),
    path('groups/', GetallGroup),
    path('upload/assignment/', PostAssignment),
]
