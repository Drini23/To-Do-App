from rest_framework import serializers
from task.models import *


class ListSerializer(serializers.ModelSerializer):
    timecomplet = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'user', 'timecomplet', 'complete']

    def get_timecomplet(self, task):
        # Replace this with your desired logic to calculate the timecomplet field
        return task.title + str(task.created)

    # def create(self, validated_data):
    #    task = Task(**validated_data)
    #    task.title = 'walk with dog'
    #    task.title = 'walk with cat'
    #    task.title = 'walk with mouse'
    #    task.save()
    #    return task


class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImages
        fields = ['id', 'image']
