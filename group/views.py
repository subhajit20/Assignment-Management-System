from multiprocessing import context
from tokenize import group
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import GroupSerializer,SearchGroupSerializer,SearchAllStudentsSerializer
from .models import Group,GroupStudentsRecord
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
    datas = {
    'userdata':request.user,
    'groupid':request.data
    }
    serializer = SearchGroupSerializer(data=request.data,context=datas)
    if serializer.is_valid():
        groupid = serializer.data.get('groupid')
        getgroup = GroupStudentsRecord.JoinGroup(groupid,request.user)
        return Response({'msg':'You have successfully joined the group...'})
    return Response({'msg':serializer.errors})

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def Get_all_Students_of_the_Group(request):
    serializer = SearchAllStudentsSerializer(data=request.data)
    if serializer.is_valid():
        groupid = serializer.data.get('groupid')
        groups = GroupStudentsRecord.Get_Group_Students(groupid)

        if group is not None:
            return Response({'msg':{'mygroups':groups}})
        else:
            return Response({'error':'Something went wrong...'})
    else:
        return Response({'msg':serializer.errors})

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def Fetch_Joined_Students_Group(request):
    if request.user is not None:
        get_joined_groups = GroupStudentsRecord.JoinedGoupLists(request)
        if get_joined_groups is not None:
            return Response({
                'msg':{
                    'groups':get_joined_groups
                }
            },status=status.HTTP_200_OK)
        else:
            return Response({
                'msg':'You have not joined any group yet...'
            },status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({
            'error':"You should be logged in..."
        },status=status.HTTP_401_UNAUTHORIZED)