from django import forms
from .models import *


class ComputerSearchForm(forms.ModelForm):
    class Meta:
        model=Computer
        fields=['users_name','IP_address','MAC_address']
class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=['first_name','last_name','user_name','email_address','password','confirm_password']

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=['user_name','email_address','password']

class CompForm(forms.ModelForm):
    class Meta:
        model=Computer
        fields=['computer_name','IP_address','MAC_address','users_name','location','purchase_date']

class updateForm(forms.ModelForm):
    class Meta:
        model=Computer
        fields=['IP_address','MAC_address','users_name']

class operatingsysForm(forms.ModelForm):
    class Meta:
        model=Operating_system 
        fields=['operating_system']      