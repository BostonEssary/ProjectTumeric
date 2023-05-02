"""ProjectTumeric URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from register import views as v
from django.urls import re_path
from accounts.views import ResetPasswordView
from django.contrib.auth import views as auth_views
from accounts.views import ChangePasswordView

urlpatterns = [
    path("", include("main.urls")),
    path("blogs/", include("blogs.urls")),
    path("reviews/", include("reviews.urls")),
    path("podcasts/", include("podcasts.urls")),
    path('', include("django.contrib.auth.urls")),
    path("register/", include("register.urls")),
    path("accounts/", include("accounts.urls")),
    path('admin/', admin.site.urls),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path("__reload__/", include("django_browser_reload.urls")),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 