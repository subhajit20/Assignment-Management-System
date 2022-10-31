from ast import Add
from django.urls import path
from .views import Create_Group,Fetch_Users_Groups,Join_Group,Get_all_Students_of_the_Group
urlpatterns = [
    path('creategroup/',Create_Group ),
    path('getusergroups/',Fetch_Users_Groups ),
    path('groupjoin/',Join_Group ),
    path('getstudents/',Get_all_Students_of_the_Group ),
]