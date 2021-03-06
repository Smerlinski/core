# Generated by Django 4.0.3 on 2022-04-07 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('end_date', models.DateField(null=True, verbose_name='project_end_date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('status', models.CharField(choices=[('Do', 'Done'), ('Du', 'During'), ('To', 'Todo')], default='To', max_length=2)),
                ('priority', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='M', max_length=1, null=True)),
                ('end_date', models.DateField(null=True, verbose_name='task_end_date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_author', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_project', to='projects.project')),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_responsible', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
