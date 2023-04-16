from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Review


class IndexView(generic.ListView):
    template_name = "reviews/index.html"
    context_object_name = "latest_review_list"

    def get_queryset(self):
        """Return the last five published reviews"""
        return Review.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
            ]
# Create your views here.

class DetailView(generic.DetailView):
    model = Review
    template_name = "reviews/detail.html"

    def get_queryset(self):
        """
        Excludes any titles that aren't published yet.
        """
        return Review.objects.filter(pub_date__lte=timezone.now())

