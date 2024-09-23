from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.contrib.auth import logout,authenticate,login
import io
from datetime import datetime
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter,A4
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import letter
#from reportlab.lib.pagesizes import landscape
#from reportlab.platypus import Image
from .utilis import send_otp
import pyotp

# Create your views here.
#@login_required
def home(request):
    title='Invoice Management System'
    context={'title':title,
             }
    if Theme.objects.filter(user=request.user.username).exists():
        color=Theme.objects.get(user=request.user.username).color
    else:
        color='lightblue'
    return render(request,'home.html')#)context,{'color':color})


@login_required
def add_invoice(request):
    title='Add Invoice Here'
    form=InvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/home/invoice_list')
    context={"title":title,
             'form':form}
    return render(request,'add.html',context)


def list(request):
    
    title='List of Invoices'
    form=InvoiceSearchForm(request.POST or None)
    
    # context={
    #       'form':form,
    #       'queryset':queryset,
    # }
    if request.method=='POST':
        name=request.POST['name']
        invoice_type=request.POST['invoice_type']
        queryset=Invoice.objects.filter(name=name,invoice_type=invoice_type)
        listcount=Invoice.objects.filter(name=name,invoice_type=invoice_type).count()
        # queryset=Invoice.objects.filter(name=form['name'].value(),invoice_type=form['invoice_type'].value()),
    else:
        queryset=Invoice.objects.all()
        listcount=queryset.count()
    
    if listcount<2 and listcount >0:
        for i in queryset:
            queryset=i
    context={'title':title,
             'queryset':queryset,
             'form':form,
             'listcount':listcount,
             }
    return render(request,'list_item.html',context)
    

# def search(request):
#     form=InvoiceSearchForm(request.POST or None)
#     if request.method=='POST':
#         queryset=Invoice.objects.filter(invoice_number__icontains=form['invoice_number'].value(),
# 									name__icontains=form['name'].value())
#         context={'form':form,
#                  'queryset':queryset,}
#     return render(request,'list_item.html',context)

def update_invoice(request, pk):
    title='Update Your Invoice Here'
    queryset = Invoice.objects.get(id=pk)
    form = InvoiceUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = InvoiceUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
                form.save()
                return redirect('/list_item')
                
        
    context = {
		'form':form,
        'title':title,
	}
    return render(request, 'update.html', context)

def delete_invoice(request,pk):
     queryset=Invoice.objects.get(id=pk)
     if request.method=='POST':
          queryset.delete()
          messages.success(request,'Deleted Successfully')
          return redirect('/list_item')
     return render(request,'delete.html')

def theme(request):
    color=request.GET.get('color')
    if color=='dark':
        if Theme.objects.filter(user=request.user.username).exists():
            user_theme=Theme.objects.get(user=request.user.username)
            user_theme.user=request.user.username
            user_theme.color='grey'
            user_theme.save()
        else:
            user2=Theme(user=request.user.username,color='grey')
            user2.save()
    elif color=='dark':
        if Theme.objects.filter(user=request.user.username).exists():
            user_theme1=Theme.objects.get(user=request.user.username)
            user_theme1.user=request.user.username
            user_theme1.color='white'
            user_theme1.save()
        else:
            user3=Theme(user=request.user.username,color='white')
            user3.save()
    

    return redirect('/')      

def genpdf(request):
    buf=io.BytesIO()
    # c=canvas.Canvas(buf,pagesize=letter,bottomup=0) 
    c=canvas.Canvas('outputfile_pdf') 
    w,h=A4
    invoices=Invoice.objects.all()
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)
    lines=[
        
    ]
   

    for invoice in invoices:
        lines.append(invoice.name)
        lines.append(invoice.invoice_type)
        lines.append(invoice.line_one)
        lines.append(invoice.line_one_quantity)
        lines.append(invoice.line_one_total_price)
        lines.append(invoice.line_two)
        lines.append(invoice.line_two_quantity)
        lines.append(invoice.line_two_total_price)
        lines.append(invoice.line_three)
        lines.append(invoice.line_three_quantity)
        lines.append(invoice.line_three_total_price)
        lines.append(invoice.line_four)
        lines.append(invoice.line_four_quantity)
        lines.append(invoice.line_four_total_price)
        
    for line in lines:
        page_number=c.getPageNumber()
        text='rebeca%s' %page_number
        #textob.textLines(lines) ,"%s" %page_number
        c.drawString(100,50,text)
                   


                   
        c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf,as_attachment=True,filename='invoices.pdf')

def otp_view(request):
    form=OtpForm(request.POST)
    error_message=None
    if request.method=='POST':
        otp=request.POST['otp']
        username=request.session['username']
        otp_secret_key=request.session['otp_secret_key']
        otp_valid_date=request.session['otp_valid_date']

        if otp_secret_key and otp_valid_date is not None:
            valid_date=datetime.fromisoformat(otp_valid_date)

            if valid_date > datetime.now():
                totp=pyotp.TOTP(otp_secret_key,interval=60)
                if totp.verify(otp):
                    user=get_object_or_404(User,username=username)
                    login(request,user)
                    del request.session['otp_secret_key']
                    del request.session['otp_valid_date']
            else:
                error_message='Invalid one-time password'
        else:
            error_message='one time password has expired'
    else:
        error_message='oops...something went wrong:('

    return render(request,'otp.html',{'error_message':error_message,'form':form})
    
def login_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        form =  UserForm(request.POST or None)
        user = authenticate(request, username=username, password=password)
        
        if user.is_authenticated:
            send_otp(request)
            request.session['username']=username
            return redirect('otp')
        else:
           error_message='Invalid username or password'
            
        
    else:
        form= UserForm()
    return render(request, 'login.html',{"form": form})



# def login_view(request):
#     form=UserForm(request.POST)
#     error_message=None
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             send_otp(request)
#             request.session['username']=username
#             return redirect('otp')
#         else:
#             error_message='Invalid username or password'
#     return render(request,'otp.html',{'error_message':error_message,'form':form})




def logout_view(request):
    logout(request)
    return redirect('login')
    

