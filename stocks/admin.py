from django.contrib import admin
from .models import *
#admin.site.register(Stock)
from .form import StockCreate

# Register your models here.
class Stockcreateadmin(admin.ModelAdmin):
    list_display =['name', 'quantity', 'price']
    form = StockCreate
    list_filter =['name']
    search_fields=['name', 'quantity'] 
    

admin.site.register(Stock, Stockcreateadmin)
admin.site.register(Category,Score)