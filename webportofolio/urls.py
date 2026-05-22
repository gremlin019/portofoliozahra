from django.urls import path
from django_distill import distill_path
from . import views
 
urlpatterns = [
    distill_path('',           views.home,       name='home',     distill_file='index.html'),
    distill_path('about/',     views.about,      name='about',    distill_file='about.html'),
    distill_path('skills/',    views.skills,     name='skills',   distill_file='skills.html'),
    distill_path('projects/',  views.projects,   name='projects', distill_file='projects.html'),
    distill_path('contact/',   views.contact,    name='contact',  distill_file='contact.html'),
]