from dataclasses import fields
from rest_framework import serializers
from .models import Group,GroupStudentsRecord

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['group_name']

class SearchGroupSerializer(serializers.Serializer):
    groupid = serializers.UUIDField()
    class Meta:
        fields = ['groupid']
    
    def validate_groupid(self,value):
        user = self.context['userdata']
        groupid = self.context['groupid']['groupid']
        print(user.user_role)
        if user.answer_upload == True and user.user_role == 'Student':
                check_group_exist = Group.objects.filter(groupid=groupid).values()
                # print(check_group_exist[0]['groupid'])
                if len(check_group_exist) > 0:
                    check_student_already_joined = GroupStudentsRecord.objects.filter(groupid=check_group_exist[0]['groupid'],studentemail=user.email).values()
                    if len(check_student_already_joined) > 0:
                            # print(check_student_already_joined)
                        raise serializers.ValidationError("You have already joined in this group...")
                    else:
                        return value
                else:
                    raise serializers.ValidationError("Group isnot exist with this id...")
        else:
            raise serializers.ValidationError("Something went wrong")

class SearchAllStudentsSerializer(serializers.Serializer):
    groupid = serializers.UUIDField()
    class Meta:
        fields = ['groupid']

