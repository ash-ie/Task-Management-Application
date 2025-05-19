from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
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