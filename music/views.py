from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests


def top_artists():
    url = "https://spotify-scraper.p.rapidapi.com/v1/chart/artists/top"

    headers = {
        "X-RapidAPI-Key": "f7836c33e5msh7b72a9ccc12699dp1aa833jsn2338b1c30d2d",
        "X-RapidAPI-Host": "spotify-scraper.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers)
    response_data = response.json()

    artists_info = []

    if "artists" in response_data:
        for artist in response_data["artists"]:
            name = artist.get("name", "No Name")
            avatar_url = artist.get("visuals", {}).get("avatar", [{}])[0].get("url", 'No URL')
            artist_id = artist.get("id", "No ID")
            artists_info.append((name, avatar_url, artist_id))
            
        return artists_info   


@login_required(login_url="login")
def index(request):
    artists_info = top_artists()
    print(artists_info)
    context = {
         'artists_info': artists_info,
    }
    return render(request, "index.html", context)


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
