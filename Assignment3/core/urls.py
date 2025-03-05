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
    path("destinations/<int:id>/", views.destroy_session, name="destinations_id"),
    path("destinations/<int:id>/destroy/", views.destroy_destination_id, name="destroy_destination_id"),


]