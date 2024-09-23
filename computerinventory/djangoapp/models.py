from django.db import models
from datetime import datetime


# Create your models here.
class Operating_system(models.Model):
    operating_system=models.CharField(max_length=30, blank=True)
    
class Computer(models.Model):
    computer_name=models.CharField(max_length=30,blank=True,null=True)
    IP_address=models.CharField(max_length=30,blank=True,null=True)
    MAC_address=models.CharField(max_length=30,blank=True,null=True)
    users_name=models.CharField(max_length=30,blank=True,null=True)
    location=models.CharField(max_length=30,blank=True,null=True)
    export_csv=models.BooleanField(default=False)
    purchase_date=models.DateTimeField("purchase_date(mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)
    def __str__(self):
         return self.computer_name


class Register(models.Model):
    first_name=models.CharField(max_length=30,null=True)
    last_name=models.CharField(max_length=30, blank=True)
    user_name=models.CharField(max_length=30,blank=True)
    email_address=models.CharField(max_length=30,null=True)
    password=models.CharField(max_length=8,null=True)
    confirm_password=models.CharField(max_length=8,null=True)

class Login(models.Model):
        user_name=models.CharField(max_length=30,blank=True)
        email_address=models.CharField(max_length=30,null=True)
        password=models.CharField(max_length=8,null=True)

class Update(models.Model):
     computer_name=models.CharField(max_length=30,blank=True,null=True)
     def __str__(self):
         return self.computer_name
     
class ComputerHistory(models.Model):
    computer_name=models.ForeignKey(Update,on_delete=models.CASCADE,blank=True)
    IP_address=models.CharField(max_length=30,blank=True,)
    MAC_address=models.CharField(max_length=30,blank=True)
    users_name=models.CharField(max_length=30,blank=True)
    location=models.CharField(max_length=30,blank=True)
    export_csv=models.BooleanField(default=False)
    purchase_date=models.DateTimeField("purchase_date(mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)
    def __str__(self):
         return self.computer_name
