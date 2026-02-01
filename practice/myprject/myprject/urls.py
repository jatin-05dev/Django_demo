"""
URL configuration for myprject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from myapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',register,name='register'),
    path('home',home,name='home'),
    path('about',about,name='about'),
    path('registerfrm',registerfrm,name='registerfrm'),
    path('login',login,name='login'),
    path('loginfrm',loginfrm,name='loginfrm'),
    path('logout',logout,name='logout'),
    path('fp',fp,name='fp'),
    path('fpfrm',fpfrm,name='fpfrm'),
    path('otp',otp,name='otp'),
    path('otpv',otpv,name='otpv'),
    path('cp',cp,name='cp'),
    path('cpfrm',cpfrm,name='cpfrm'),
    path('home2',home2,name='home2'),

















]
