from django.urls import path

from . import views

app_name = ""
urlpatterns = [
    path("", views.StaticView.as_view(), name="index"),
]