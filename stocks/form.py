from django import forms
from .models import*

class StockCreate(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('name', 'quantity', 'price','issued_to','received_by')
    def clean_category(self):
      name = self.cleaned_data.get('name')
      if not name:
        raise forms.ValidationError('This field is required')
      return name
      for instance in Stock.objects.all() :
        if instance.name == name:
          raise forms.ValidationError(name, "already exists")
        return name
        
        
        


    def clean_item_name(self):
      quantity = self.cleaned_data.get('quantity')
      if not quantity:
        raise forms.ValidationError('This field is required')
      return quantity
class StockSearchForm(forms.ModelForm):
   export_to_CSV = forms.BooleanField()
   class Meta:
     model = Stock
     fields = ['name', 'quantity']
     
     
class updateform(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['name', 'quantity', 'price']
class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['issued_quantity', 'issued_to','date_issued']


class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['received_quantity', 'received_by','date_received']
class ReorderLevelForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['reorder_level']


