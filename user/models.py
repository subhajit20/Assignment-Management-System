from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import (
    make_password,
    check_password
)
from django.db import connection
from .MyUserManager import MyUserManager


# Create your models here.
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(("password"), max_length=128)
    user_role = models.CharField(max_length=100,editable=True,blank=True)
    assignment_upload = models.BooleanField(default=False)
    answer_upload = models.BooleanField(default=False)
    firstname = models.CharField(max_length=200,editable=True,blank=True)
    lastname = models.CharField(max_length=200,editable=True,blank=True)
    stream = models.CharField(max_length=200,editable=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    objects = MyUserManager()

    @classmethod
    def CreateAccount(cls,email,password,userrole):
        hasedpassword = make_password(password)
        if userrole == "Teacher":
            newuser = cls.objects.create(email=email,password=hasedpassword,user_role=userrole,assignment_upload=True,answer_upload=True)
            newuser.save()
        if userrole == "Student":
            newuser = cls.objects.create(email=email,password=hasedpassword,user_role=userrole,assignment_upload=False,answer_upload=True)
            newuser.save()
        return True
    
    @classmethod
    def GetUser(cls,email,password):
        get_user = cls.objects.get(email=email)
        dcrypted_password = check_password(password,get_user.password)
        # print(dcrypted_password)
        if get_user and dcrypted_password:
            return {'flag':True,'user':get_user}
        else:
            return {'flag':False,'user':'No students are there'}

    @classmethod
    def Get_user_email(cls,email):
        user = cls.objects.get(email=email)
        if user is not None:
            return user
        else:
            return False
    
    @classmethod
    def Change_Password(cls,email,password):
        hasedpassword = make_password(password)
        getuser = cls.Get_user_email(email=email)
        if getuser != False:
            with connection.cursor() as cursor:
                cursor.execute('UPDATE user_user SET password = %s WHERE email = %s',[hasedpassword,getuser.email])
                row = cursor.close()
            return True
        else:
            return False

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

