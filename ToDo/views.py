from django.shortcuts import render
from todoapp.models import Task

def home(request):
    task = Task.objects.filter(iscompleted= False).order_by("-updated_at")
    print(task)
    context = {
        'task' : task,
    }
    return render(request, 'home.html', context = context)