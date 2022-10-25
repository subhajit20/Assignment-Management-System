from pstats import Stats
from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.serializer import RegisterSerailzer,LoginSerializer
from rest_framework import status
from .models import User


# Registration View
@api_view(['POST'])
def Registration(request):
    if request.method == 'POST':
        serializer = RegisterSerailzer(data=request.data)

        if serializer.is_valid():
            print(serializer.data)
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            userrole = serializer.data.get("user_role")
            newuser = User.CreateAccount(email,password,userrole)

            if newuser:
                return Response({'success':'Successfully created account...'},status=status.HTTP_200_OK)
            else:
                return Response({'error':'Something went wrong...'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def Login(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data,context=request.data)

        if serializer.is_valid():
            print(serializer.data)
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            newuser = User.GetUser(email=email,password=password)
            if newuser['flag']:
                print(newuser['user'])
                return Response({'success':'Successfully created account...',"user":newuser['user'].email},status=status.HTTP_200_OK)
            else:
                return Response({'error':'Something went wrong...'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)