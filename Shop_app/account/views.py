from django.shortcuts import redirect, render
from .forms import UserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was successfully registered for" + user)
            return redirect("user_login")
    
    context = {
        'form' : form
    }

    return render(request, 'register.html', context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request, "Username or password incorrect")
                    
    else:
        form = LoginForm()

    context = {
        'form' : form
    }

    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('index')