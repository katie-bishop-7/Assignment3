from django.shortcuts import render

def index(request):
    return render(request, "core/index.html")

def new_user(request):
    return render(request, "core/new_user.html")

def new_session(request):
    return render(request, "core/index.html")

def user(request):
    return render(request, "core/index.html")

def sessions(request):
    return render(request, "core/index.html")

def destroy_session(request):
    return render(request, "core/index.html")

def destinations(request):
    return render(request, "core/index.html")

def new_destination(request):
    return render(request, "core/index.html")

def destination_id(request):
    return render(request, "core/index.html")

def destroy_destination_id(request):
    return render(request, "core/index.html")