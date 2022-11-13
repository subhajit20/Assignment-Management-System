from django.db import models
# Create your models here.
from django.db import models
from django.utils.timezone import now
import os
from uuid import uuid4
import random
from datetime import datetime
from user.models import User

def user_directory_path(instance, filename):
    # Get Current Date
    todays_date = datetime.now()

    path = "uploads/{}/{}/{}/".format(todays_date.year, todays_date.month, todays_date.day)
    extension = "." + filename.split('.')[-1]
    stringId = str(uuid4())
    randInt = str(random.randint(10, 99))

    # Filename reformat
    filename_reformat = stringId + randInt + extension

    return os.path.join(path, filename_reformat)

# Create your models here.
class Assignment(models.Model):
    assignmentID = models.AutoField(primary_key=True,unique=True)
    assignmenttoken = models.UUIDField(default=uuid4())
    assignmentName = models.CharField(max_length=200,editable=True,blank=True)
    assignmentDesc = models.CharField(max_length=200,editable=True,blank=True)
    assignmentFile = models.FileField(upload_to=user_directory_path)
    assignmentuser = models.ForeignKey(User,on_delete=models.CASCADE)
    upload_time = models.DateTimeField(default=now)
    groupID = models.UUIDField(blank=True)
    submissionTime = models.DateTimeField(blank=True)