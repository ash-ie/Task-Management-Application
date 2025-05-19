from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages

from superadmin_app.forms import UserForm
from superadmin_app.models import User
# Create your views here.
def signin(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                if user.role == 1:
                    return redirect('superadmin_home')
                elif user.role == 2:
                    return redirect('admin_home')
            else:
                messages.info(request, 'Invalid Credentials')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
    return render(request, 'login.html')

def superadmin_index(request):
    return render(request,'superadmintemp/index.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm

def add_users(request):
    try:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.is_active = True
                user.save()
                return redirect('view_users')
        else:
            form = UserForm()
        return render(request, 'superadmintemp/user_form.html', {'form': form})
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        form = UserForm() 
        return render(request, 'superadmintemp/user_form.html', {'form': form})

def view_users(request):
    try:
        data = User.objects.exclude(role=1)
        return render(request, 'superadmintemp/users.html', {'data': data})
    except Exception as e:
        messages.error(request, f"An error occurred while fetching users: {str(e)}")
        return render(request, 'superadmintemp/users.html', {'data': []})

def delete_user(request, user_id):
    try:
        user = get_object_or_404(User, id=user_id)
        user.delete()
        messages.success(request, "User deleted successfully.")
    except Exception as e:
        messages.error(request, f"An error occurred while deleting the user: {e}")
    return redirect('view_users') 
