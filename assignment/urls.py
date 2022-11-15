from django.urls import path
from .views import PostAssignment
urlpatterns = [
    # path('home/', GetAllUser),
    # path('groups/', GetallGroup),
    path('upload/assignment/', PostAssignment),
]
