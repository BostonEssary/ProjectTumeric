from django.urls import path
from .views import home, RegisterView  # Import the view here
from .views import profile
from django.urls import re_path
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('', home, name='accounts-home'),
    path('register/', RegisterView.as_view(), name='accounts-register'),  # This is what we added
    path('profile/', profile, name='accounts-profile'),
    re_path('login/', auth_views.LoginView.as_view(), name='accounts-login')
]   
