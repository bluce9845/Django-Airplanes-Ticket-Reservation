from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticated
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In...")
            return redirect('home')
        else:
            messages.success(request, "There Wa An Error Logging, Please Try Again.....")
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You Have Successfully Register...")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

      
def logout_user(request):
    logout(request)
    return redirect('home')