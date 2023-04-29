from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect    
from .forms import LoginForm, AvatarForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views import generic


# Create your views here.
class ProfileView(generic.TemplateView):
    
    template_name = "profile.html"
   
    
        

    def profile(request, username):
        
        if request.user.is_authenticated:
            username = request.user.username
            username = None
            context = {}
            context['form'] = AvatarForm()
            return render(request, "accounts/profile.html", context)
        else:
            return HttpResponseRedirect('/accounts/not-logged-in')
            
        


def not_logged_in(request):
    
    return render(request, template_name='accounts/notloggedin.html') 


def logout_view(request):
    logout(request)
    return redirect("/")

