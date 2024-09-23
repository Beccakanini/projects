from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.urls import reverse
 

# Create your views here.
def home(request):
    title='Computer Inventory Management System'
    context={"title":title}
    return render(request,'home.html',context)
    

def computer_entry(request):
    title='Add Computer'
    form=CompForm(request.POST or None)
    if form.is_valid():
        form.save()
        #form.save_m2m()
        messages.success(request,"Saved Successfully")
        return redirect('/computer_entry')
    context={'title':title,
            'form':form,
                 }
    return render(request,'computer_entry.html',context)
    
def complist(request):
    title='List of all computers'
    form=ComputerSearchForm(request.POST or None)
    queryset=Computer.objects.all()
    context={"title":title,
             'queryset':queryset,
             'form':form}
    if request.method=="POST":
        queryset=Computer.objects.filter()
        #if form['export_to_CSV'].value() == True:
            #response = HttpResponse(content_type='text/csv')
            #response['Content-Disposition'] = 'attachment; filename="Computer list.csv"'
            #writer = csv.writer(response)
            #writer.writerow(['COMPUTER NAME', 'IP Address', 'MAC ADDRESS', 'OS', 'USERNAME', 'LOCATION', 'PURCHASE DATE', 'TIMESTAMP'])
            #nstance = queryset
        #for row in instance:
         #writer.writerow([row.computer_name, row.IP_address, row.MAC_address, row.operating_system.all(), row.users_name, row.location])
       # return response
         #context={'title':title,
        #'queryset':queryset,
       # 'form':form,}
    return render(request,'complist.html',context)

def get_absolute_url(self):
   return reverse("comp_edit", kwargs={"id": self.id})

def comp_edit(request,pk):  
    title='Edit your details here'
    queryset=Computer.objects.get(id=int(pk))
    form=updateForm(instance=queryset)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,"Updated Successfully")
            return redirect('/complist')
    context={'form':form,
             'title':title,
             }
    return render(request,'computer_entry.html',context)  
def comp_delete(request,pk):
    queryset=Computer.objects.get(id=int(pk))
    if request.method=='POST':
        queryset.delete()
        messages.success(request,"Deleted Successfully")
        return redirect('/complist')
    
    return render(request,'delete.html')
def register(request):
    title="Register Here"
    form=RegisterForm(request.POST or None)
    if request.method=="POST" and form.is_valid:
        form.save()
        messages.success(request,"Registration was successful")
    context={'title':title,
             'form':form,
            }
    return render(request,'register.html',context)
def login(request):
    title="Sign In"
    form=LoginForm(request.POST or None)
    if request.method=="POST" and form.is_valid:
        form.save()
        messages.success(request,"Registration was successful")
    context={
        'title':title,
        'form':form
    }
    return render(request,'login.html',context)
def settings(request):
    title = 'Add operating system'
    form = operatingsysForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/computer_list')
    context = {
   "title": title,
   "form": form,
    }   
    return render(request, "settings.html",context)