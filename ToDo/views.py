from django.shortcuts import render
from todoapp.models import Task

def home(request):
    task = Task.objects.filter(iscompleted= False).order_by("-updated_at")
    completed_task = Task.objects.filter(iscompleted=True).order_by("-updated_at")
    # print(task)
    context = {
        'task': task,
        'c_task': completed_task,
    }
    return render(request, 'home.html', context = context)