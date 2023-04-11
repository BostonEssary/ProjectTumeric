from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Title


class IndexView(generic.ListView):
    template_name = "blogs/index.html"
    context_object_name = "latest_title_list"

    def get_queryset(self):
        """Return the last five published blogs"""
        return Title.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
            ]
    
class DetailView(generic.DetailView):
    model = Title
    template_name = "blogs/detail.html"

    def get_queryset(self):
        """
        Excludes any titles that aren't published yet.
        """
        return Title.objects.filter(pub_date__lte=timezone.now())
