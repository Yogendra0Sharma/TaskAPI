from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None,use_url=True)
    doc = serializers.FileField(max_length=None,use_url=True)

    class Meta:
        model =  Task
        fields = ('id','task_name','task_desc','completed','date_created','image','doc')

