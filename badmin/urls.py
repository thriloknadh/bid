"""bid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.views.generic import TemplateView

from badmin import views



urlpatterns = [
    path('admin/',admin.site.urls),
    path('admin_login/',TemplateView.as_view(template_name="badmin_templates/admin_login.html"),name="admin_login"),
    path('admin_home/',TemplateView.as_view(template_name="badmin_templates/admin_home.html"),name="admin_home"),
    path('admin_savedetails/',views.saveDetails,name='admin_savedetails'),
    path('pending_reg/',views.pending_reg,name="pending_reg"),
    path('approved_reg/',views.approved_reg,name="approved_reg"),
    path('declined_reg/',views.declined_reg,name="declined_reg"),
    path('approved/',views.approved,name="approved"),
    path('declined/',views.declined,name="declined"),
    path('logout/',views.logout,name="logout")
 ]
