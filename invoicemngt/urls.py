"""
URL configuration for invoicemngt project.

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
from invoiceapp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    #path('accounts/login/',home),
    path('home/add/', add_invoice),
    path('home/invoice_list/', list),
    path('delete<str:pk>/',delete_invoice),
    path("home/search/",list),
    path("home/theme/",theme),
    path("home/genpdf/",genpdf),
    path("login/",login_view),
    path("otp/",otp_view),             
    path('login_view/',login_view,name='login_view'),


    path("logout/",logout_view),
    path('accounts/',include('invoiceapp.urls')),
    path('accounts/',include('registration.backends.default.urls')),
]

