"""
URL configuration for computerinventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from djangoapp.views import register,home,login,computer_entry,complist,comp_delete,comp_edit

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    path('',home),
    path('computer_entry/',computer_entry),
    path('complist/',complist),
    path('complist/edit<str:pk>/',comp_edit),
    path('complist/delete<str:pk>/',comp_delete),
    path('home/register/',register),
    path('home/login/',login),
    path('accounts/',include('registration.backends.default.urls')),
    path('home/search/',complist),
    path('settings/',complist),
    ]
