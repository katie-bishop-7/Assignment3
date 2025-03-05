from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import User, Session, Destination
from django.contrib.auth.hashers import make_password, check_password

def index(request):
    return render(request, "core/index.html")

def new_user(request : HttpRequest):
    print("New user")
    return render(request, "core/new_user.html")

def new_session(request):
    return render(request, "core/new_session.html")

def user(request : HttpRequest):
    print("user endpoint")
    if request.method == 'POST':
        params = request.POST
        user = User(
            name = params.get("name"),
            email = params.get("email"),
            password_hash = make_password(params.get("password"))
        )
        # TODO: basic data validation
        # TODO: create session
        user.save()
        return redirect("../destinations/")

    return render(HttpResponse("404: Page not found"))

def sessions(request):
    return render(request, "core/index.html")

def destroy_session(request):
    return render(request, "core/index.html")

def destinations(request : HttpRequest):
    if request.method == "GET":
        destinations = Destination.objects.all()
        return render(request, "core/destinations.html", {"destinations" : destinations})
    if request.method == "POST":
        print("post destinations")
        params = request.POST
        destination = Destination(
            place = params.get("place"),
            review = params.get("review"),
            rating = params.get("rating")
        )
        # TODO: basic data validation
        destination.save()
        return render(request, "core/destinations.html", {"destinations" : destinations})


def new_destination(request):
    return render(request, "core/new_destination.html")

def destination_id(request):
    return render(request, "core/index.html")

def destroy_destination_id(request):
    return render(request, "core/index.html")