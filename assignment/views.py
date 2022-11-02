from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import User
from group.models import Group
from django.core.cache import cache
from django.conf import settings
from rest_framework import status
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
