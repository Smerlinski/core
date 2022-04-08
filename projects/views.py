from django.shortcuts import render
from rest_framework import viewsets
from .models import Project, Tasks
from .serializers import ProjectSerializer, TaskSerializer

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
