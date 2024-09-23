from django.urls import path
from .import views

urlpatterns=[path('',views.home,name='home'),
             path('home/add/',views.add_invoice,name='add_invoice'),
             path('home/invoice_list/',views.list,name='invoice_list'),
             path('update<str:pk>/',views.update_invoice,name='update'),
             path('delete<str:pk>/', views.delete_invoice, name="delete"),
             path('home/theme',views.theme,name='theme'),
             #path("home/genpdf/",views.genpdf,name="genpdf"),
             path("home/search/",views.list,name="search"),
             path("home/genpdf/",views.genpdf,name="genpdf"),
             path('login_view/',views.login_view,name='login_view'),
             path('otp/',views.otp_view,name='otp'),
             path('logout/',views.logout_view,name='logout_view'),
]
            