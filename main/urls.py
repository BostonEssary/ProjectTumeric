from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("", views.StaticView.as_view(), name="index"),
] 