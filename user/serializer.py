from dataclasses import fields
from rest_framework import serializers
from .models import User
class RegisterSerailzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','user_role']
    
    def validate_user_role(self,value):
        if value == "Teacher" or value == "Student":
            return value
        else:
            raise serializers.ValidationError("Invalid usertype! If You are a student then choose Student or if you are a Teacher then choose Teacher")
