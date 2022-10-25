from django.urls import path
from .views import Registration


urlpatterns = [
    path('r1/', Registration),
]
