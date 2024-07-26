from django.db import models

class OfficeTask(models.Model):

    taskname = models.CharField(max_length=200)
    priority= models.CharField(max_length=10)
    duedate= models.DateField()
    estimatedtime= models.TimeField()
    notes= models.CharField(max_length=800)
    completed= models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskname

    

class HouseholdTask(models.Model):

    taskname = models.CharField(max_length=200)
    priority= models.CharField(max_length=50)
    room= models.CharField(max_length=80)
    equipment= models.CharField(max_length=550)
    assignee= models.CharField(max_length=300)
    notes= models.CharField(max_length=800)
    completed= models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskname


class SideskillsTask(models.Model):

    taskname = models.CharField(max_length=200)
    skillcategory= models.CharField(max_length=100)
    goal= models.CharField(max_length=100)
    resources= models.CharField(max_length=500)
    timeallocation= models.CharField(max_length=200)
    notes= models.CharField(max_length=800)
    completed= models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskname


class WorkoutTask(models.Model):

    taskname = models.CharField(max_length=200)
    type= models.CharField(max_length=80)
    duration= models.CharField(max_length=90)
    location= models.CharField(max_length=200)
    equipment= models.CharField(max_length=550)
    goal= models.CharField(max_length=100)
    notes= models.CharField(max_length=800)
    completed= models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskname