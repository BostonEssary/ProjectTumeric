from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from .models import AvatarForm
from django.views import generic

# Create your views here.
class ProfileView(generic.TemplateView):
    
    template_name = "profile.html"
   
    def avatar_form(request):
        return render(request, 'profile.html', {'form': AvatarForm()} )

    def profile(request, username="default"):
        return render(request, "accounts/profile.html")







def login(response):
    if response.method == "POST":
        form = LoginForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = LoginForm()

    return render(response, "accounts/login.html", {"form":form})