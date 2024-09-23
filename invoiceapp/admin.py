from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display=['name', 'invoice_number', 'invoice_date']
    list_filter=['name']
    search_fields=['name', 'invoice_number']
admin.site.register(Invoice)
admin.site.register(Theme)