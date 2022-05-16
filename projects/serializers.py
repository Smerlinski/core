from django.shortcuts import get_object_or_404
from .models import Project, Tasks
from rest_framework import serializers
from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()
    id = serializers.ModelField(model_field=Project()._meta.get_field('id'))

    class Meta:
        model = Project
        fields = ['author', 'name', 'description', 'end_date', 'id']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author = get_object_or_404(CustomUser, email=author_data['email'])
        project = Project.objects.create(author=author, **validated_data)
        return project

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()
        return instance


class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    author = CustomUserSerializer()
    responsible = CustomUserSerializer()

    class Meta:
        model = Tasks
        fields = ['id','project', 'author', 'responsible', 'name', 'description', 'status', 'priority', 'end_date']

    def create(self, validated_data):
        project_data = validated_data.pop('project')
        author_data = validated_data.pop('author')
        responsible_data = validated_data.pop('responsible')
        project = get_object_or_404(Project, id=project_data['id'])
        author = get_object_or_404(CustomUser, email=author_data['email'])
        responsible = get_object_or_404(CustomUser, email=responsible_data['email'])
        task = Tasks.objects.create(project=project, author=author, responsible=responsible, **validated_data)
        return task

    def update(self, instance, validated_data):
        project_data = validated_data.pop('project')
        author_data = validated_data.pop('author')
        responsible_data = validated_data.pop('responsible')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()
        return instance
