from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import User, Session, Destination
from django.contrib.auth.hashers import make_password
import secrets

def index(request):
    all_destinations = Destination.objects.filter(share_publicly=True)
    if all_destinations:
        # TODO: figure this out
        top_5_destinations = []
        for i in range(5):
            top_5_destinations.append(all_destinations[i])
        
    return render(request, "core/index.html", {"destinations": all_destinations})

def new_user(request : HttpRequest):
    return render(request, "core/new_user.html")

def new_session(request : HttpRequest):
    return render(request, "core/new_session.html")

def user(request : HttpRequest):
    if request.method == 'POST':

        # get name, email, password from POST request
        params = request.POST
        name = params.get("name")
        email = params.get("email")
        password = params.get("password")

        # basic data validation
        if "@" not in email:
            return HttpResponse("Invalid email address")
        if len(password) < 8:
            return HttpResponse("Password must be at least 8 characters")
        if not any(char.isdigit for char in password):
            return HttpResponse("Password must contain at least one number")
        
        # try to create a user
        try:
            user = User(
                name = name,
                email = email,
                password_hash = make_password(password)
            )
        except (Exception):
            print("exception")
            return HttpResponse(Exception)
        user.save()

        # create a session
        session = Session(
            token = secrets.token_hex(32),
            user = user
        )
        session.save()
        res = redirect("../destinations/")
        res.set_cookie("token", session.token)
       
        # TODO: check session
        return res

    return HttpResponse("404: Page not found")


def sessions(request : HttpRequest):
    if request.method == 'POST':
        print("POST REQUEST")
        email = request.COOKIES.get("email", "") # "" is the default value
        print(email)
        user = User.objects.filter(email=email)
        print(user)
        print("user == true", user == True)
        if not user: # if user does not exist
            return HttpResponse("Invalid username or password")
        else:
            return redirect("../destinations/")
    return render(request, "core/index.html")

def destroy_session(request):
    return render(request, "core/index.html")

def destinations(request : HttpRequest):
    if request.method == "GET":
        destinations = Destination.objects.all()
        return render(request, "core/destinations.html", {"destinations" : destinations})
    if request.method == "POST":
        params = request.POST
        destination = Destination(
            place = params.get("place"),
            review = params.get("review"),
            rating = params.get("rating"),
            share_publicly = params.get("share-publicly")
        )
        # TODO: basic data validation
        destination.save()
        return redirect('/destinations/')


def new_destination(request):
    return render(request, "core/new_destination.html")

def destination_id(request):
    return render(request, "core/index.html")

def destroy_destination_id(request):
    return render(request, "core/index.html")