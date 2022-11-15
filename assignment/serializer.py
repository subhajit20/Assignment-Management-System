from rest_framework import serializers
from .models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['assignmentName','assignmentFile']
    
    def validate_assignmentName(self,value):
        if value is None or value == "":
            raise serializers.ValidationError("Assignment Name is Null")
        elif len(value) < 3:
            raise serializers.ValidationError("Assignment Name is too small...")
        else:
            return value