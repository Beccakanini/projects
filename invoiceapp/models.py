from django.db import models


# Create your models here.

class Invoice(models.Model):
	comments = models.TextField(max_length=3000, default='', blank=True, null=True)
	invoice_number = models.CharField(blank=True, null=True,max_length=120)
	invoice_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	name = models.CharField('Customer Name', max_length=120, default='', blank=True, null=True)
	
	line_one = models.CharField('Line 1', max_length=120, default='', blank=True, null=True)
	line_one_quantity = models.CharField('Quantity', default=0, blank=True, null=True,max_length=120)
	line_one_unit_price = models.CharField('Unit Price (D)', default=0, blank=True, null=True,max_length=120)
	line_one_total_price = models.CharField('Line Total (D)', default=0, blank=True, null=True,max_length=120)

	line_two = models.CharField('Line 2', max_length=120, default='', blank=True, null=True)
	line_two_quantity = models.CharField('Quantity', default=0, blank=True, null=True,max_length=120)
	line_two_unit_price = models.CharField('Unit Price (D)', default=0, blank=True, null=True,max_length=120)
	line_two_total_price = models.CharField('Line Total (D)', default=0, blank=True, null=True,max_length=120)

	line_three = models.CharField('Line 3', max_length=120, default='', blank=True, null=True)
	line_three_quantity = models.CharField('Quantity', default=0, blank=True, null=True,max_length=120)
	line_three_unit_price = models.CharField('Unit Price (D)', default=0, blank=True, null=True,max_length=120)
	line_three_total_price = models.CharField('Line Total (D)', default=0, blank=True, null=True,max_length=120)

	line_four = models.CharField('Line 4', max_length=120, default='', blank=True, null=True)
	line_four_quantity = models.CharField('Quantity', default=0, blank=True, null=True,max_length=120)
	line_four_unit_price = models.CharField('Unit Price (D)', default=0, blank=True, null=True,max_length=120)
	line_four_total_price = models.CharField('Line Total (D)', default=0, blank=True, null=True,max_length=120)

	phone_number = models.CharField(max_length=120, default='', blank=True, null=True)
	total = models.CharField(default='0', blank=True, null=True ,max_length=120)
	balance = models.CharField(default='0', blank=True, null=True,max_length=120)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
	paid = models.BooleanField(default=False)
	invoice_type_choice = (
			('Receipt', 'Receipt'),
			('Proforma Invoice', 'Proforma Invoice'),
			('Invoice', 'Invoice'),
		)
	invoice_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)

	def __unicode__(self):
		return self.invoice_number
	
	invoice_type_choice = (
		('Invoice', 'Invoice'),
		('Receipt', 'Receipt'),
		('Proforma Invoice', 'Proforma Invoice'),
	)
	invoice_type = models.CharField(max_length=50, blank=True, null=True, choices=invoice_type_choice)

class Theme(models.Model):
		color=models.CharField(max_length=1000)
		user=models.CharField(max_length=1000)

		def __str__(self):
			return self.user
		
class User(models.Model):
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	
class Otp(models.Model):
	otpnum=models.CharField(max_length=60)



	