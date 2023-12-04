from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images')
    desc = models.TextField()
    price = models.IntegerField()


class Travel_courses(models.Model):
    coursename = models.CharField(max_length=100)
    img = models.ImageField(upload_to='courseimages')
    desc = models.TextField()
    link = models.URLField(max_length=200)


class Tourism_courses(models.Model):
    coursename = models.CharField(max_length=100)
    img = models.ImageField(upload_to='courseimages')
    desc = models.TextField()
    link = models.URLField(max_length=200)


class Hospitality_courses(models.Model):
    coursename = models.CharField(max_length=100)
    img = models.ImageField(upload_to='courseimages')
    desc = models.TextField()
    link = models.URLField(max_length=200)


class Profile(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


'''class Hotels(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='hotelimages')
    ratings = models.CharField(max_length=5)'''

