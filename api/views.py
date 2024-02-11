from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .serializers import *
from task.models import *
from django.contrib.auth.models import User


# Create your views here.


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return[AllowAny()]
        return[IsAuthenticated()]

    def get_serializer_context(self):
        return {'request': self.request}

    def delete(self, request, id):
        task = get_object_or_404(Task, pk=id)

        if not task.complete:
            return Response({"error": 'Task is not completed, so it cannot be deleted'},
                            status=status.HTTP_400_BAD_REQUEST)

        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskImage(ModelViewSet):
    serializer_class = TaskImageSerializer

    def get_queryset(self):
        return TaskImages.objects.filter(task_id=self.kwargs['task_pk'])