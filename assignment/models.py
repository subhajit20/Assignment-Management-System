from django.db import models
# Create your models here.
from django.db import models
from django.utils.timezone import now
import os
import uuid
import random

from datetime import datetime

def user_directory_path(instance, filename):
    # Get Current Date
    todays_date = datetime.now()

    path = "uploads/{}/{}/{}/".format(todays_date.year, todays_date.month, todays_date.day)
    extension = "." + filename.split('.')[-1]
    stringId = str(uuid.uuid4())
    randInt = str(random.randint(10, 99))

    # Filename reformat
    filename_reformat = stringId + randInt + extension

    return os.path.join(path, filename_reformat)

# Create your models here.
class Assignment(models.Model):
    assignmentID = models.AutoField(primary_key=True,unique=True)
    assignmentName = models.CharField(max_length=200,editable=True,blank=True)
    assignmentFile = models.FileField(upload_to=user_directory_path)
    upload_time = models.DateTimeField(default=now)
    groupID = models.UUIDField(blank=True)
    submissionTime = models.DateTimeField(blank=True)

    @classmethod
    def CreateAssignment(cls,**kargs):
        newassignemnt = cls.objects.create(assignmentName=kargs['assignmentName'],assignmentFile=kargs['assignmentFile'])
        newassignemnt.save()

        return True