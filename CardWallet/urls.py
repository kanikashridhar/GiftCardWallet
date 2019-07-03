"""CardWallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    

    path('signup/', TemplateView.as_view(template_name="signup.html"),name='signup'),
    path('email-verification/',TemplateView.as_view(template_name="email_verification.html"),name='email-verification'),
    path('login/', TemplateView.as_view(template_name="login.html"),name='login'),
    path('logout/', TemplateView.as_view(template_name="logout.html"),name='logout'),
    path('password-reset/',TemplateView.as_view(template_name="password_reset.html"),name='password-reset'),
    path('password-reset/confirm/', TemplateView.as_view(template_name="password_reset_confirm.html"), name='password-reset-confirm'),
    path('user-details/',TemplateView.as_view(template_name="user_details.html"),name='carddetails'),
    path('password-change/',TemplateView.as_view(template_name="password_change.html"),name='password-change'),

    path('', include('CardsApi.urls')),
    path('', include('django.contrib.auth.urls')),
    path('rest-auth/', include('rest_auth.urls')),


]
