from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
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
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:  # Check if passwords match
            # Check if the username is unique
            if not User.objects.filter(username=username).exists():
                # Check if the email is unique
                if not User.objects.filter(email=email).exists():
                    # Create and save the user
                    user = User.objects.create_user(username=username, email=email, password=password1)

                    # Log in the user
                    login(request, user)
                    return redirect('login')  # Replace 'login' with the actual URL name or path for your login page
                else:
                    error_message = "Email is already registered."
            else:
                error_message = "Username is already taken."
        else:
            error_message = "Passwords do not match."

        return render(request, 'signup.html', {'error_message': error_message})

     return render(request, 'signup.html')                    
