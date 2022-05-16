from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Project, Tasks
from .serializers import ProjectSerializer, TaskSerializer

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=True)
    def get(self, request, pk=None):
        queryset = Tasks.objects.filter(project=pk)
        serializer_class = TaskSerializer(queryset, many=True)
        return Response(serializer_class.data)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
