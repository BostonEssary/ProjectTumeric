from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Podcast
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'podcasts/index.html'
    context_object_name = "latest_title_list"

    def get_queryset(self):
        """Return the last five published blogs"""
        return Podcast.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
            ]
    
class DetailView(generic.DetailView):
    model = Podcast
    template_name = "podcasts/detail.html"
