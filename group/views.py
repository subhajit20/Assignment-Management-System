from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import GroupSerializer,SearchGroupSerializer
from .models import Group,GroupMember
from rest_framework import status

# Create your views here.

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def Create_Group(request):
    serializer = GroupSerializer(data=request.data)
    print(request.user.user_role)
    if serializer.is_valid():
        groupname = serializer.data.get('group_name')
        create_new_group = Group.Group_Create(groupname,request.user)
        if create_new_group:
            return Response({'msg':'Group is created succesfully'},status=status.HTTP_201_CREATED) 
        else:
            return Response({'msg','Something went wrong'},status=status.HTTP_400_BAD_REQUEST)
    return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def Fetch_Users_Groups(request):
    if request.user is not None:
        getgroups = Group.Get_Current_user_group(request.user)
        print(getgroups)
        if getgroups is not None:
            return Response({'groups':getgroups},status=status.HTTP_302_FOUND)
        else:
            return Response({'error':'No groups are availabe...'},status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'msg':'Your are not authorized...'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def Join_Group(request):
    serializer = SearchGroupSerializer(data=request.data)
    if serializer.is_valid():
        groupid = serializer.data.get('groupid')
        getgroup = GroupMember.JoiningGroups(groupid,request.user)
        print(getgroup)
        return Response({'msg':"Group founded..."})
    return Response({'msg':serializer.errors})

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def Get_all_Students_of_the_Group(request):
    data = GroupMember.Get_Group_Students()

    print(data[1]['groupname'])
    return Response({'msg':data})
