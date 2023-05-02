from django.urls import path
from .views import home, RegisterView  # Import the view here
from .views import profile

app_name = 'accounts'
urlpatterns = [
    path('', home, name='accounts-home'),
    path('register/', RegisterView.as_view(), name='accounts-register'),  # This is what we added
    path('profile/', profile, name='accounts-profile'),
]   
