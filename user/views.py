from turtle import delay
from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.serializer import RegisterSerailzer,LoginSerializer,EmailSerailizer,PasswordSerializer
from rest_framework import status
from .models import User
from .lib.JWTTOKENGenerator import get_tokens_for_user
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from .tasks import Sending_Emails,Sending_Emails_For_Reseting_Password


# Registration View
@api_view(['POST'])
def Registration(request):
    if request.method == 'POST':
        serializer = RegisterSerailzer(data=request.data)

        if serializer.is_valid():
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            userrole = serializer.data.get("user_role")
            newuser = User.CreateAccount(email,password,userrole)
            if newuser:
                Sending_Emails.delay(email_handle=email)
                return Response({'success':'Successfully created account...'},status=status.HTTP_200_OK)
            else:
                return Response({'msg':"Not Found"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error':"Something went wrong..."},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def Login(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data,context=request.data)

        if serializer.is_valid():
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = User.GetUser(email=email,password=password)
            if user['flag']:
                print(user)
                token = get_tokens_for_user(user['user'])
                print(token)
                return Response({'success':'Successfully created account...',"user":user['user'].email,"token":token},status=status.HTTP_200_OK)
            else:
                return Response({'error':'Something went wrong...'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def Request_ResetPassword(request):
    if request.method == "POST":
        serializer = EmailSerailizer(data=request.data)
        if serializer.is_valid():
            useremaill = serializer.data.get("email")
            getuseremail = User.Get_user_email(email=useremaill)
            if getuseremail != False:
                token = get_tokens_for_user(getuseremail)
                print(token['access'])
                reset_password_link = str(f'http://127.0.0.1:8000/user/resetpassword/{token["access"]}')
                Sending_Emails_For_Reseting_Password.delay(email_handle=useremaill,link=reset_password_link)
                return Response({'msg':"An message has been sent to your mail"},status=status.HTTP_200_OK)
        else:
            return Response({'error':serializer.errors},status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def Reset_Password(request):
    serializer = PasswordSerializer(data=request.data,context=request.data)
    if serializer.is_valid():
        password = serializer.data.get("newpassword")
        flag = User.Change_Password(request.user.email,password)
        if flag:
            return Response({'msg':"Password has successfully been reset..."},status=status.HTTP_200_OK)
        return Response({'msg':"Password has not successfully been reset..."},status=status.HTTP_404_NOT_FOUND)
    return Response({'msg':serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
