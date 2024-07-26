from django import forms 
from django.forms import ModelForm

from .models import OfficeTask, WorkoutTask, SideskillsTask, HouseholdTask


class OfficeTaskForm(forms.ModelForm):

    class Meta:

        model = OfficeTask
        fields = ['taskname', 'priority', 'duedate', 'estimatedtime', 'notes', 'completed']


class WorkoutTaskForm(forms.ModelForm):

    class Meta:

        model = WorkoutTask
        fields = ['taskname', 'type', 'duration', 'location', 'equipment', 'goal', 'notes', 'completed']


class SideskillsTaskForm(forms.ModelForm):

    class Meta:

        model = SideskillsTask
        fields = ['taskname', 'skillcategory', 'goal', 'resources', 'timeallocation', 'notes', 'completed']


class HouseholdTaskForm(forms.ModelForm):

    class Meta:

        model = HouseholdTask
        fields = fields = ['taskname', 'priority', 'room', 'equipment', 'assignee', 'notes', 'completed']