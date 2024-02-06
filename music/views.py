from django.contrib.auth import authenticate, login, logout
from .models import Artist
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
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
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:  # Check if passwords match
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect("signup")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect("signup")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect("/")

        else:
            messages.info(request, "password not matching")
            return redirect("signup")

    else:
        return render(request, "signup.html")


def logout(request):
    pass
