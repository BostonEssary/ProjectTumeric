from django.urls import path
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"
urlpatterns = [
path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

] 





 