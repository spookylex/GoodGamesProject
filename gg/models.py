from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank = True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

class Profile(models.Model):
    name = models.OneToOneField(User, max_length = 25, on_delete = models.CASCADE)
    username = models.CharField(max_length=50)
    socialMediaLinks = models.CharField(max_length=200)
    playsOn = models.CharField(max_length = 50)
    favoriteGames = models.TextField(default="")

class Review(models.Model):
    username = models.CharField(max_length=50)
    gameTitle = models.CharField(max_length=100)
    reviewTitle = models.CharField(max_length=100)
    reviewBody = models.TextField(max_length=10000)
    rating = models.CharField(max_length=1000)



