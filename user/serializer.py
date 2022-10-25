from dataclasses import fields
from rest_framework import serializers
from .models import User
from django.db import connection
from django.contrib.auth.hashers import (
    check_password
)
class RegisterSerailzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','user_role']
    
    def validate_user_role(self,value):
        if value == "Teacher" or value == "Student":
            return value
        else:
            raise serializers.ValidationError("Invalid usertype! If You are a student then choose Student or if you are a Teacher then choose Teacher")

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_email(self,value):
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM user_user WHERE email = %s',[value])
            row = cursor.fetchone()
        
        if row:
            return value
        else:
            raise serializers.ValidationError("Email is  invalid...")
    
    def validate_password(self,value):
        email = self.context.get('email')
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM user_user WHERE email = %s',[email])
            row = cursor.fetchone()
            dcryptedpassword = check_password(value,row[3])
        print(dcryptedpassword)
        if row and dcryptedpassword:
            return value
        else:
            raise serializers.ValidationError("Email and Password is  invalid...")