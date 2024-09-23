from django.urls import path
from . import views

urlpatterns = [  
        path('', views.home,name='home'), 
        path("computer_entry/", views.computer_entry,name='computer_entry'),
        path("complist/", views.complist,name='complist'),
        path("complist/edit/<str:pk>",views.comp_edit,name="edit"),
        path("complist/delete/<str:pk>",views.comp_delete,name="delete"),
        path("register/",views.register,name="register"),
        path("login/",views.login,name="login"),
        path("search/",views.complist,name="search"),
        path("settings/",views.settings,name="settings"),
]   

