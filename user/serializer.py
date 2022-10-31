import configparser
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
        if value is None:
            raise serializers.ValidationError("Invalid usertype! If You are a student then choose Student or if you are a Teacher then choose Teacher")
        else:
            raise serializers.ValidationError("Invalid usertype! If You are a student then choose Student or if you are a Teacher then choose Teacher")

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        fields = ['email','password']

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

class EmailSerailizer(serializers.Serializer):
    email = serializers.EmailField()
    class Meta:
        fields = ['email']

    def validate_email(self,value):
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM user_user WHERE email = %s',[value])
            row = cursor.fetchone()
        
        if row is not None:
            return value
        else:
            raise serializers.ValidationError("Email is invalid...")

class PasswordSerializer(serializers.Serializer):
    newpassword = serializers.CharField(max_length=50)

    class Meta:
        fields = ["newpassword","confirmpassword"]
    
    def validate_newpassword(self,value):
        confirmpassword = self.context.get("confirmpassword")
        if value == confirmpassword:
            return value
        else:
            raise serializers.ValidationError("Passwords are not matched")