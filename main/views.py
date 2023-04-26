from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.generic import TemplateView
from django.utils import timezone


 
# Create your views here.
class StaticView(TemplateView):
    template_name = "main/index.html" 