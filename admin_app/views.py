from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from admin_app.decorators import admin_required
from superadmin_app.forms import TaskForm
from superadmin_app.models import Task

# Create your views here.
@admin_required
def admin_index(request):
    return render(request,'admintemp/index.html')

@admin_required
def add_task(request):
    try:
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('view_task_admin')
        else:
            form = TaskForm()
        return render(request, 'admintemp/task_form.html', {'form': form})
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        form = TaskForm() 
    return render(request, 'admintemp/task_form.html', {'form': form})

@admin_required
def view_task(request):
    try:
        data = Task.objects.all()
        return render(request, 'admintemp/tasks.html', {'data': data})
    except Exception as e:
        messages.error(request, f"An error occurred while fetching tasks: {str(e)}")
        return render(request, 'admintemp/tasks.html', {'data': []})

@admin_required    
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully.")
            return redirect('view_task_admin')
    else:
        form = TaskForm(instance=task)
    return render(request, 'admintemp/task_edit.html', {'form': form})

@admin_required
def delete_task(request, task_id):
    try:
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        messages.success(request, "Task deleted successfully.")
    except Exception as e:
        messages.error(request, f"An error occurred while deleting the user: {e}")
    return redirect('view_task_admin') 