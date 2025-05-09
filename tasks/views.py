from django.shortcuts import render, redirect
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
