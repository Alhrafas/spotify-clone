from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Artist
from django.contrib.auth.models import User
from django.db.models import Count


def get_top_artists():
    # Retrieve the top artists based on the number of albums they have
    top_artists = Artist.objects.annotate(num_albums=Count('album')).order_by('-num_albums')[:10]
    return top_artists

@login_required(login_url="login")
def index(request):
    top_artists = get_top_artists()
    return render(request, "index.html", {'top_artists': top_artists})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password.")
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
                messages.error(request, "Email already taken.")
                return redirect("signup")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken.")
                return redirect("signup")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                login(request, user)
                return redirect("/")
        else:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

    return render(request, "signup.html")


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect("login")
