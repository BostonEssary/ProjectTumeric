from django.urls import path

from . import views
from .views import ProfileView


app_name = "accounts"

urlpatterns = [
    path("login", views.login, name="index"),
    path('profile/<slug:username>/', ProfileView.profile, name="profile"),
]