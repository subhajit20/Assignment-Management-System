from dataclasses import fields
from rest_framework import serializers
from .models import Group,GroupMember

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['group_name']

class SearchGroupSerializer(serializers.Serializer):
    groupid = serializers.UUIDField()
    class Meta:
        fields = ['groupid']
    