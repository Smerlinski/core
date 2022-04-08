from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Project(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='project_author')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    end_date = models.DateField(null=True, verbose_name='project_end_date')

    def __str__(self):
        return self.name

class Priority(models.TextChoices):
    HIGH = "H", "High"
    MEDIUM = "M", "Medium"
    LOW = "L", "Low"

class Status(models.TextChoices):
    DONE = "Do", "Done"
    DURING = "Du", "During"
    TODO = "To", "Todo"

class Tasks(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='task_project')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='task_author')
    responsible = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='task_responsible')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.TODO)
    priority = models.CharField(max_length=1, choices=Priority.choices, default=Priority.MEDIUM, null=True)
    end_date = models.DateField(null=True, verbose_name='task_end_date')

    def __str__(self):
        return self.name
