"""expertreviewprj URL Configuration

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
from django.urls import path
from expertreviewapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('common',views.common),
    path('register',views.register),
    path('login',views.login),
    path('about',views.about),
    path('contact',views.contact),
    path('admin_dashboard',views.admin),
    path('addcars',views.addcars),
    path('managecars',views.managecars),
    path('manageusers',views.manageusers),
    path('manageexperts',views.manageexperts),
    path('queries',views.queries),
    path('nosuchuser',views.nosuchuser),
    path('expert_dashboard',views.experthome),
    path('user_dashboard',views.userhome),

    
]
