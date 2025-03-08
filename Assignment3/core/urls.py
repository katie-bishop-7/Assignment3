from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users/new/", views.new_user, name="new_user"),
    path("sessions/new/", views.new_session, name="new_session"),
    path("users/", views.user, name="user"),
    path("sessions/", views.sessions, name="sessions"),
    path("sessions/destroy/", views.destroy_session, name="destroy_session"),
    path("destinations/", views.destinations, name="destinations"),
    path("destinations/new/", views.new_destination, name="new_destinations"),
    path("destinations/<int:id>/", views.destination_id, name="destination_id"),
    path("destinations/<int:id>/destroy/", views.destroy_destination_id, name="destroy_destination_id"),


]