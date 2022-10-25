from django.urls import path
from .views import Registration,Login


urlpatterns = [
    path('register/', Registration),
    path('login/', Login),
]
