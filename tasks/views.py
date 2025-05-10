from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description", "")
        if title:
            Task.objects.create(title=title, description=description)
            return redirect("task_list")
        else:
            error = "Title is required."
            return render(
                request, "tasks/task_list.html", {"tasks": tasks, "error": error}
            )
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("task_list")
