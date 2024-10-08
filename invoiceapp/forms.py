from django import forms
from .models import *

class InvoiceForm(forms.ModelForm):
    class Meta:
        model=Invoice
        fields=['name', 'phone_number', 'invoice_date','invoice_type',
				'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
				'line_two', 'line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
				'line_three', 'line_three_quantity', 'line_three_unit_price', 'line_three_total_price',
				'total', 'paid',
				]
class InvoiceSearchForm(forms.ModelForm):
    class Meta:
        model=Invoice
        fields=['name','invoice_type']
        
def clean_invoice_number(self):
		invoice_number = self.cleaned_data.get('invoice_number')
		if not invoice_number:
			raise forms.ValidationError('This field is required')
		return invoice_number


def clean_name(self):
		name = self.cleaned_data.get('name')
		if not name:
			raise forms.ValidationError('This field is required')
		return name

class InvoiceUpdateForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['invoice_number','name','invoice_type']

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','password',]
class OtpForm(forms.ModelForm):
	class Meta:
		model=Otp
		fields=['otpnum']