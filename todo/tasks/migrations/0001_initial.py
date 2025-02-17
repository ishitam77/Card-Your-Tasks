# Generated by Django 5.0.7 on 2024-07-16 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseholdTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=200)),
                ('priority', models.CharField(max_length=10)),
                ('room', models.CharField(max_length=30)),
                ('equipment', models.CharField(max_length=250)),
                ('assignee', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OfficeTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=200)),
                ('priority', models.CharField(max_length=10)),
                ('duedate', models.CharField(max_length=30)),
                ('estimatedtime', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SideskillsTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=200)),
                ('skillcategory', models.CharField(max_length=10)),
                ('goal', models.CharField(max_length=30)),
                ('resources', models.CharField(max_length=250)),
                ('timeallocation', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=10)),
                ('duration', models.CharField(max_length=30)),
                ('intensity', models.CharField(max_length=250)),
                ('locatioin', models.CharField(max_length=200)),
                ('equipment', models.CharField(max_length=250)),
                ('goal', models.CharField(max_length=30)),
                ('notes', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
