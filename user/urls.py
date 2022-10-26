from django.urls import path
from .views import Registration,Login,Request_ResetPassword,Reset_Password


urlpatterns = [
    path('register/', Registration),
    path('login/', Login),
    path('requestresetpassword/', Request_ResetPassword),
    path('resetpassword/', Reset_Password),
]
