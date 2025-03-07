from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password_hash = models.CharField(max_length=500)
    destination = models.ForeignKey("Destination", on_delete=models.CASCADE, related_name="destination")

class Session(models.Model):
    token = models.CharField(max_length=500)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="session_user")

class Destination(models.Model):
    name = models.CharField(max_length=100)
    review = models.CharField(max_length=5000)
    rating = models.SmallIntegerField()
