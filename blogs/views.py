from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Blog




class IndexView(generic.ListView):
    template_name = "blogs/index.html"
    context_object_name = "latest_blog_list"
    
    def get_queryset(self):
        """Return the last five published blogs"""
        return Blog.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
            ]
    
class DetailView(generic.DetailView):
    model = Blog
    template_name = "blogs/detail.html"
 
    def get_queryset(self):
        """
        Excludes any titles that aren't published yet.
        """
        return Blog.objects.filter(pub_date__lte=timezone.now())
