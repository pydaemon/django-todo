from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    filter_type = request.GET.get("filter", "all")
    if filter_type == "completed":
        tasks = tasks.filter(completed=True)
    elif filter_type == "not_completed":
        tasks = tasks.filter(completed=False)
    tasks = tasks.order_by("-created_at")
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description", "")
        if title:
            Task.objects.create(user=request.user, title=title, description=description)
            return redirect("task_list")
        else:
            error = "Title is required."
            return render(
                request, "tasks/task_list.html", {"tasks": tasks, "error": error}
            )
    return render(
        request, "tasks/task_list.html", {"tasks": tasks, "filter_type": filter_type}
    )


@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect("task_list")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("task_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})
