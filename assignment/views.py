from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from user.models import User
from group.models import Group
from django.core.cache import cache
from django.conf import settings
from rest_framework import status
from .serializer import AssignmentSerializer
from .models import Assignment
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.cache.backends.base import DEFAULT_TIMEOUT
# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@api_view(['GET'])
def GetAllUser(request):
    if 'myusers' in cache:
        products = cache.get('myusers')
        print("From Chaching ---------> ")
        return Response(products, status=status.HTTP_201_CREATED)
    # return Response({
    #     'msg':'No datas'
    # },status=status.HTTP_404_NOT_FOUND)
    else:
        users = User.objects.all().values()
        user = cache.set('myusers',users,30)
        print("From Database  ---------> ")
        return Response({
        'msg':users
        })

@api_view(['GET'])
def GetallGroup(request):
    if 'groups' in cache:
        products = cache.get('groups')
        print("From Chaching ---------> ")
        return Response(products, status=status.HTTP_201_CREATED)
    # return Response({
    #     'msg':'No datas'
    # },status=status.HTTP_404_NOT_FOUND)
    else:
        users = Group.objects.all().values()
        user = cache.set('groups',users,30)
        print("From Database  ---------> ")
        return Response({
        'msg':users
        })

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def PostAssignment(request):
    serializer = AssignmentSerializer(data=request.data)
    if serializer.is_valid():
        data = {
        "assignmentName":serializer.data.get("assignmentName"),
        "assignmentFile":request.FILES['assignmentFile'],
        "user":request.user
        }
        flag = Assignment.Upload(**data)
        if flag:
            return Response({
            'msg':'Assignment is successfully uploded ...'
            })
        else:
            return Response({
                'msg':'Assignment is not successfully uploded'
                })
    return Response({
    'msg':serializer.errors
    })