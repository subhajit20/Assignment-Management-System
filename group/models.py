from email.policy import default
from enum import auto, unique
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


class GroupStudentsRecord(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    groupname = models.CharField(max_length=100,editable=True)
    groupid = models.URLField()
    studentid = models.IntegerField(editable=True)
    studentemail = models.EmailField()
    joiningtime = models.DateTimeField(default=now)

    @classmethod
    def JoinGroup(cls,groupid,student):
        try:
            if student.answer_upload == True and student.user_role == 'Student':
                check_group_exist = Group.objects.filter(groupid=groupid).values()
                # print(check_group_exist[0]['groupid'])
                if len(check_group_exist) > 0:
                    check_student_already_joined = cls.objects.filter(groupid=check_group_exist[0]['groupid'],studentemail=student.email).values()
                    if len(check_student_already_joined) > 0:
                        # print(check_student_already_joined)
                        return False
                    else:
                        print(student)
                        create_entry = cls.objects.create(
                            groupname=check_group_exist[0]['group_name'],
                            groupid=check_group_exist[0]['groupid'],
                            studentid=student.id,
                            studentemail=student.email
                        )
                        create_entry.save()
                        return True
                else:
                    return None 
        except Exception as e:
            return None
    @classmethod
    def Get_Group_Students(cls,groupid):
        try:
            is_group = cls.objects.filter(groupid=groupid).values()

            if len(is_group) > 0:
                return is_group
            else:
                return None
        except Exception as e:
            return None
    
    @classmethod
    @classmethod
    def JoinedGoupLists(cls,student):
        try:
            if student.user_role == 'Student' and student.answer_upload == True:
                get_all_groups = cls.objects.filter(studentemail=student.email).values()
                if len(get_all_groups) > 0:
                    return get_all_groups
                else:
                    return None
            else:
                return None
        except Exception as e:
            return None