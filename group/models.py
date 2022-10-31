from email.policy import default
from user.models import User
from django.db import models
from uuid import uuid4
from django.utils.timezone import now

class Group(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    groupid = models.UUIDField(default=uuid4())
    group_name = models.CharField(max_length=100,editable=True)
    group_creator = models.ForeignKey(User,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True,editable=True)
    group_members = models.IntegerField(default=0,editable=True)

    def __str__(self):
        return self.group_name

    @classmethod
    def Group_Create(cls,groupname,groupcreator):
        try:
            if groupcreator.user_role == 'Teacher' and groupcreator.assignment_upload == True:
                newgroup = cls.objects.create(group_name=groupname,group_creator=groupcreator)
                newgroup.save()
                return True
            return False
        except Exception as e:
            print(e)
            return False
    
    @classmethod
    def Get_Current_user_group(cls,groupcreator):
        try:
            if groupcreator.user_role == 'Teacher' and groupcreator.assignment_upload == True:
                get_groups = cls.objects.filter(group_creator=groupcreator).values()
                if len(get_groups) > 0:
                    return get_groups
                else:
                    return None
            return None
        except Exception as e:
            print(e)
            return None


class GroupMember(models.Model):
    joinId = models.AutoField(primary_key=True,unique=True)
    groupname = models.ForeignKey(Group,on_delete=models.CASCADE)
    members = models.ForeignKey(User,on_delete=models.CASCADE)
    joined = models.DateTimeField(default=now,editable=False)
    can_upload_answer = models.BooleanField(default=True,editable=False)


    @classmethod
    def JoiningGroups(cls,group_id,student):
        try:
            if student.user_role == 'Student' and student.answer_upload == True:
                get_groups = Group.objects.get(groupid=group_id)
                if get_groups:
                    try:
                        add_entry = cls.objects.create()
                        add_entry.groupname.add(get_groups)
                        add_entry.members.add(student)
                        add_entry.save()
                        return True
                    except Exception as e:
                        print(e)
                        return None
                else:
                    return None
            return None
        except Exception as e:
            print(e)
            return None

    @classmethod
    def Get_Group_Students(cls):
        getgroup_members = cls.objects.all().values()

        return getgroup_members



