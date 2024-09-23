"""
URL configuration for stockmngt project.

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
from stocks import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path ('', views.home, name='home'),
    path ('list/', views.list, name='list'),
     path ('add_item/', views.add_item, name='add_item'),
    path('update_items/<str:pk>', views.update_items, name="update_items"),
    path('delete/<str:pk>', views.delete, name="delete"),
    path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
    path('issue_items/<str:pk>', views.issue_items, name="issue_items"),
    path('receive_items/<str:pk>', views.receive_items, name="receive_items"),
    path('reorder_level/<str:pk>', views.reorder_level, name="reorder_level"),
    path('accounts/', include('registration.backends.default.urls')),



    path('admin/', admin.site.urls)
]
 