from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.
def login(response):
    if response.method == "POST":
        form = LoginForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = LoginForm()

    return render(response, "accounts/login.html", {"form":form})