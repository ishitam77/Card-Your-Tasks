from django.shortcuts import render, redirect

from django.http import HttpResponse

from . models import OfficeTask, WorkoutTask, SideskillsTask, HouseholdTask

from . forms import OfficeTaskForm, HouseholdTaskForm, WorkoutTaskForm, SideskillsTaskForm

from django.contrib import messages

#home page
def index(request):

    office_tasks= OfficeTask.objects.all()

    workout_tasks= WorkoutTask.objects.all()

    sideskills_tasks= SideskillsTask.objects.all()

    household_tasks=HouseholdTask.objects.all()

    context = {

        'office_tasks': office_tasks,

        'workout_tasks': workout_tasks,

        'sideskills_tasks': sideskills_tasks,

        'household_tasks': household_tasks,

        'task_type_office': 'office',

        'task_type_workout': 'workout',

        'task_type_sideskills': 'sideskills',

        'task_type_household': 'household',
        
    }

    return render(request, "index.html", context)


#form to create tasks 
def create_task(request):

    task_type = request.GET.get('type')  # Get task type from GET request

    if task_type == 'office':

        form_class = OfficeTaskForm

    elif task_type == 'household':

        form_class = HouseholdTaskForm

    elif task_type == 'sideskills':

        form_class = SideskillsTaskForm

    elif task_type == 'workout':

        form_class = WorkoutTaskForm

    form = form_class()

    if request.method == "POST":

        form = form_class(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your Task is Scheduled!!")

            return redirect("index")

    context = {'form': form, 'task_type': task_type}

    return render(request, 'create-task.html', context=context)


#update the secheduled task
def update_task(request, pk, task_type):

    if task_type == 'office':

        task = OfficeTask.objects.get(id=pk)

        form_class = OfficeTaskForm

    elif task_type == 'household':

        task = HouseholdTask.objects.get(id=pk)

        form_class = HouseholdTaskForm

    elif task_type == 'sideskills':

        task = SideskillsTask.objects.get(id=pk)
        
        form_class = SideskillsTaskForm

    elif task_type == 'workout':

        task = WorkoutTask.objects.get(id=pk)

        form_class = WorkoutTaskForm

    form = form_class(instance=task) #creates a form instance pre-filled with the existing task instance

    if request.method == "POST": #form has been submitted

        form = form_class(request.POST, instance=task) #creates a form instance, pre-filled with the POST data and the existing task instance

        if form.is_valid():

            form.save()

            messages.success(request, "Task updated successfully!")

            return redirect("index")

    context={'form': form, 'task': task, 'task_type': task_type}

    return render(request, 'update-task.html', context=context)


#delete the scheduled task
def delete_task(request, pk, task_type):

    if task_type == 'office':

        task = OfficeTask.objects.get(id=pk)

    elif task_type == 'household':

        task = HouseholdTask.objects.get(id=pk)

    elif task_type == 'sideskills':

        task = SideskillsTask.objects.get(id=pk)

    elif task_type == 'workout':

        task = WorkoutTask.objects.get(id=pk)

    task.delete()

    messages.success(request, "Task deleted successfully!")

    return redirect("index")


#search a task according to thei taskname 
def search_task(request):

    if request.method == 'GET':

        taskname = request.GET.get('taskname')

        which_task = request.GET.get('which-task')

        tasks = None

        if taskname or which_task:

            if which_task == 'office':

                tasks = OfficeTask.objects.filter(taskname__icontains=taskname)

            elif which_task == 'household':

                tasks = HouseholdTask.objects.filter(taskname__icontains=taskname)

            elif which_task == 'sideskills':

                tasks = SideskillsTask.objects.filter(taskname__icontains=taskname)

            elif which_task == 'workout':
                
                tasks = WorkoutTask.objects.filter(taskname__icontains=taskname)

    context = {'tasks': tasks, 'which_task': which_task}
        
    return render(request, 'search-task.html', context=context)