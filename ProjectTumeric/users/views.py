from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone


class RegisterView(generic.ListView):
    template_name = "registration/registration.html"

class IndexView(generic.ListView):
    template_name = "registration/login.html"
    
    
      