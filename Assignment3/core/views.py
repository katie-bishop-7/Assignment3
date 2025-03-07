from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import User, Session, Destination
from django.contrib.auth.hashers import make_password
import secrets

def index(request):
    token = request.COOKIES.get("token")
    if token:
        session = Session.objects.filter(session_token=token).first()
        if session:
            return redirect("/destinations/")
        else:
            return redirect("/sessions/new/")
    else:
        all_destinations = Destination.objects.filter(share_publicly=True)
        top_5_destinations = []

        for i in range(len(all_destinations)):
            if len(top_5_destinations) < 5:
                top_5_destinations.append(all_destinations[i])
            
        return render(request, "core/index.html", {"destinations": top_5_destinations})

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
        if email in [user.email for user in User.objects.all()]:
            return HttpResponse("Email already taken")
        # try to create a user
        try:
            password_hash = make_password(password)
            print(password, password_hash)
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
            session_token = secrets.token_hex(32),
            user = user
        )
        session.save()
        res = redirect("../destinations/")
        res.set_cookie("token", session.session_token)
       
        # TODO: check session
        return res

    return HttpResponse("404: Page not found")


def sessions(request : HttpRequest):
    if request.method == 'POST': # USER LOGS IN WITH EMAIL AND PASSWORD
        email = request.POST.get("email", "") # "" is the default value
        user = User.objects.filter(email=email).first()
        
        if not user: # if user does not exist
            return HttpResponse("Invalid username or password")
        else:
            # if user has a session, redirect to destinations
            session = Session.objects.filter(user=user).first()
            if session:
                session.session_token = secrets.token_hex(32)
            else:
                # if user does not have a session, create one
                session = Session(
                    session_token = secrets.token_hex(32),
                    user = user
                    )
            session.save()
            res = redirect("../destinations/")
            res.set_cookie("token", session.session_token)
            return res
            
    return render(request, "core/index.html")

def destroy_session(request : HttpRequest):
    response = redirect("../../")
    response.delete_cookie("token")
    return response

def destinations(request : HttpRequest):
    token = request.COOKIES.get("token")
    session = Session.objects.filter(session_token=token).first()
    if not session:
        return redirect("/sessions/new/")
    user = session.user

    if request.method == "GET":
        if user:
            destinations = Destination.objects.filter(user=user)
        else:
            destinations = None
        return render(request, "core/destinations.html", {"destinations" : destinations})
    if request.method == "POST":
        params = request.POST
        if params.get("share-publicly"):
            share_publicly = True
        else:
            share_publicly = False

        destination = Destination(
            place = params.get("place"),
            review = params.get("review"),
            rating = params.get("rating"),
            share_publicly = share_publicly,
            user = user
        )
        # data validation
        if not destination.place:
            return HttpResponse("Please enter a place")
        if not destination.review:
            return HttpResponse("Please enter a review")
        if not destination.rating:
            return HttpResponse("Please enter a rating")
        destination.save()
        return redirect('/destinations/')


def new_destination(request):
    return render(request, "core/new_destination.html")

def destination_id(request):
    return render(request, "core/index.html")

def destroy_destination_id(request):
    return render(request, "core/index.html")