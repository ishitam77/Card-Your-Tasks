from django.contrib import admin

from .models import OfficeTask, WorkoutTask, SideskillsTask, HouseholdTask

admin.site.register(OfficeTask)
admin.site.register(WorkoutTask)
admin.site.register(SideskillsTask)
admin.site.register(HouseholdTask)