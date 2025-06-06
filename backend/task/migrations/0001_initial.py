# Generated by Django 5.1.4 on 2025-01-22 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0002_alter_projectstatus_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_status', models.CharField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Task statuses',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=254, unique=True)),
                ('start_date', models.DateField(blank=True, default=None, null=True)),
                ('due_date', models.DateField(blank=True, default=None, null=True)),
                ('completed_date', models.DateField(blank=True, default=None, null=True)),
                ('project', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.project')),
                ('task_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.taskstatus')),
            ],
        ),
    ]
