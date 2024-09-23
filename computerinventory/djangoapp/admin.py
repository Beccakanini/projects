from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.


class ComputerAdmin(admin.ModelAdmin):
    list_display=['computer_name','IP_address','MAC_address','users_name','location','purchase_date','timestamp']
    form=CompForm
    list_filter=['computer_name','IP_address','users_name']
    search_fields=['computer_name','IP_address']
class RegisterUser(admin.ModelAdmin):
    list_display=['first_name','last_name','user_name','email_address','password','confirm_password']
    form=RegisterForm
    list_filter=['user_name','email_address']
    search_fields=['user_name','email_address']

class LoginUser(admin.ModelAdmin):
    list_display=['user_name','email_address','password']
    form=LoginForm
    list_filter=['user_name','email_address']
    search_fields=  ['user_name','email_address'] 
admin.site.register(Computer,ComputerAdmin)
admin.site.register(Register,RegisterUser)
admin.site.register(Login,LoginUser)
admin.site.register(Update)
