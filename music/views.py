from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Artist, Song, Album
from django.contrib.auth.models import User
from django.db.models import Count


def get_top_artists():
    # Retrieve the top artists based on the number of albums they have
    top_artists = Artist.objects.annotate(num_albums=Count("album")).order_by(
        "-num_albums"
    )[:10]
    return top_artists


def get_top_songs():
    # Retrieve the top songs based on the number of times they've been played
    top_songs = Song.objects.annotate(num_plays=Count("plays")).order_by("-num_plays")[
        :18
    ]
    return top_songs

def play_song(request, song_id):
    # Retrieve the song object from the database
    song = get_object_or_404(Song, pk=song_id)

    # Additional logic for playing the song can be added here

    # Pass the song object to the template
    return render(request, 'music.html', {'song': song})

@login_required(login_url="login")
def index(request):
    top_artists = get_top_artists()
    top_songs = get_top_songs()

    #     dividing the list into three part
    firt_six_sogns = top_songs[0:6]
    second_six_songs = top_songs[6:12]
    third_six_songs = top_songs[12:18]
    
    context = {
         'top_artists': top_artists,
         'first_six_songs': firt_six_sogns,
         'second_six_songs': second_six_songs,
         'third_six_songs': third_six_songs,
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


def profile(request, artist_id):
     artist = get_object_or_404(Artist, pk=artist_id)
     albums = Album.objects.filter(artist=artist)
     songs = Song.objects.filter(album__in=albums)
     return render(request, "profile.html", {'artist': artist, 'songs': songs})


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
