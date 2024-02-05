from django.contrib.auth import authenticate, login, logout
from .models import Artist
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("passowrd")

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            return redirect("index")

        else:
            return render(request, "login.html", {"error": "Invlid credantials"})

    return render(request, "login.html")


def profile(request):
    return render(request, "profile.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:  # Check if passwords match
             print('password same')
             
        else:
             messages.info(request, "password not matching")
             return redirect('singup')   

    else:
        return render(request, "signup.html")


def logout(request):
    pass
