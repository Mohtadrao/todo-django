from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task,)
    return redirect('home')

def markDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.iscompleted = True
    task.save()
    return redirect('home')

def unmarkDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.iscompleted = False
    task.save()
    return redirect('home')

def edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        t = request.POST['task']
        task.task=t
        task.save()
        return redirect('home')
    else:
        context = {
            'task': task,
        }
        return render(request, "edit_task.html", context)

def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("home")