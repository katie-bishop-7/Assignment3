from django.http import HttpRequest
from .models import Session, User
from django.shortcuts import redirect

def authenticate_user_middleware(next):

    def middleware(request : HttpRequest):
        # Read the session_token out of the cookie
        session_token = request.COOKIES.get("session_token")
        
        # Find the session by its token
        session = Session.objects.filter(session_token=session_token).first()

        # Get the user from the session and attach it to the request.
        if session:
            request.user = session.user
        else:
            request.user = None

        # If URI maps to an endpoint requires a user to be logged in and there is no session, redirect them to the /sessions/new page
        
        log_in_uris = ["destinations/",
                       "sessions/destroy/", 
                       "destinations/new", 
                       "destinations/<int:id>/", 
                       "destinations/<int:id>/destroy/"
                       ]
        if request.path in log_in_uris and not session:
            return redirect("sessions/new/")
        else:
            return(next(request))
        
    return middleware
