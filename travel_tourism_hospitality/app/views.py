from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from . import models



def home(request):
    return render(request, 'home.html')


def courses(request):
    return render(request, 'courses.html')


def bookings(request):
    dests = models.Destination.objects.all()
    return render(request, 'bookings.html', {'dests': dests})





def profile(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        user = User.objects.get(first_name=first_name)
        user = auth.authenticate(first_name=first_name)
        if user is not None:
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/')
    else:
        return render(request, 'profile.html')


def course(request, coursetype):
    if coursetype == "travel":
        courses = models.Travel_courses.objects.all()
    elif coursetype == "tourism":
        courses = models.Tourism_courses.objects.all()
    elif coursetype == "hospitality":
        courses = models.Hospitality_courses.objects.all()
    return render(request, 'course.html', {'courses': courses})
