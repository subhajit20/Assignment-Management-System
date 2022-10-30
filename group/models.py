from email.policy import default
from user.models import User
from django.db import models
from uuid import uuid4
from django.utils.timezone import now

class Group(models.Model):
    id = models.AutoField(primary_key=True,unique=True,default=uuid4())
    group_name = models.CharField(max_length=100,editable=True)
    group_creator = models.ForeignKey(User,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True,editable=True)
    group_members = models.IntegerField(default=0,editable=True)


class GroupMember(models.Model):
    groupId = models.AutoField(primary_key=True,unique=True)
    groupname = models.ManyToManyField(Group)
    members = models.ManyToManyField(User)
    joined = models.DateTimeField(default=now,editable=False)
    can_upload_answer = models.BooleanField(default=True,editable=False)




