from django.db import models
from django.utils import timezone
from twilio.rest import Client
import os



name = (
		('Furniture', 'Furniture'),
		('IT Equipment', 'IT Equipment'),
		('Phone', 'Phone'),
	)


#name= models.CharField(max_length=100, blank=True, null=True, choices=name)
class Category(models.Model):
    
	name = models.CharField(max_length=100, blank=True, null=True)
	def __str__(self):
		return self.name
class Stock(models.Model):
    name = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True) 
    quantity = models.PositiveIntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    issued_quantity = models.PositiveIntegerField(null=True)
    issued_to= models.CharField(max_length=100,blank=False,null=False)
    date_issued =models.DateField(default=timezone.now)
    received_quantity = models.PositiveIntegerField(null=True)
    received_by= models.CharField(max_length=100,blank=False, null= False)
    date_received= models.DateField(default=timezone.now)
    reorder_level= models.PositiveIntegerField(null=True,unique=True)
    #issued_by = models.CharField(max_length=100)

    #created_at = models.DateTimeField(auto_now_add=True) 
    #updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        pass
    #    return self.name, " " ,str(self.quantity) ," ", str(self.price)," ", self.issued_to, "" ,self.received_by




# Create your models here.
class Score(models.Model):
      result=models.PositiveIntegerField()

      def __str__(self):
            return str(self.result)
      
      def save(self,*args,**kwargs):
            if self.result < 70:
                account_sid = os.environ['AC0bdbf1f09547433489b1855fe699c5b1']
                auth_token = os.environ['ed5b1450aed26007a86eadf07e357ce1']
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                     body="Welcome! Sending SMS with Twilio. You won!",
                     from_='+15017122661',
                     to='+254 796 419278'
                    )

                print(message.sid)
                return super().save(*args,**kwargs)
                  
            
