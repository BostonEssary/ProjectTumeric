from django.urls import path

from . import views
from .views import ProfileView


app_name = "accounts"

urlpatterns = [
    path('profile/<slug:username>/', ProfileView.profile, name="profile"),
    path('logout', views.logout_view, name='logout'),
    path('not-logged-in', views.not_logged_in, name="not-logged-in")
]