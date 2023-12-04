from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('courses', views.courses, name='courses'),
    path('bookings', views.bookings, name='bookings'),
    path('profile', views.profile, name='profile'),
    path('addprofile', views.profile, name='profile'),
    path('courses/<coursetype>', views.course, name='course'),


]