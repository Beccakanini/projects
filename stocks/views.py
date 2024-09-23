from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import csv
from django.views.decorators.csrf import csrf_exempt

from .form import *
from .models import *


def home(request):
    title = ' stock management system'.upper()
    context = {
        'title': title,
    }

    return render(request, 'home.html', context)
@login_required
def list(request):
    header = 'list of items'.upper()
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        'header': header,
        'queryset': queryset,
        'form': form

    }

    if request.method == 'POST':
        queryset = Stock.objects.filter(  name=form['name'].value()
        #quantity=form['quantity'].value()
        )
          
        # if form['export_to_CSV'].value() == True:
        #     response = HttpResponse(content_type='text/csv')
        #     response['Content-Disposition'] = 'attachment; filename="stock.csv"'
        #     writer = csv.writer(response)
        #     writer.writerow(['name', 'quantity', 'price','timestamp', 'last_update'])
        #     instance = queryset
        #     for stock in instance:
        #         writer.writerow([stock.name, stock.quantity, stock.price,stock.timestamp,stock.last_updated])
        #     return response
    context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }

    return render(request, 'list.html', context)

@login_required

def add_item(request):
    title = 'add item'
    form = StockCreate(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Added succefully')
        return redirect('/list')
    context = {
        'title': 'add items',
        'form': form}
    return render(request, 'add_item.html', context)

def reorder_level(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReorderLevelForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Reorder level for " + str(instance.name) + " is updated to " + str(instance.reorder_level))

		return redirect("/list")
	context = {
			"instance": queryset,
			"form": form,
		}
	return render(request, "add_item.html", context)



def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = updateform(instance=queryset)
    if request.method == 'POST':
        form = updateform(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'updated succefully')
            return redirect('/list')


    context = {
        'form': form
}
    return render(request, 'add_item.html', context)


def delete(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/list')
    return render(request, 'delete.html')

def stock_detail(request, pk):
	queryset = Stock.objects.get(id=pk)
	context = {
		"title": queryset.name,
		"queryset": queryset,
	}
	return render(request, "detaal.html", context)

def issue_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = IssueForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity -= instance.issued_quantity
		instance.issue_by = str(request.user)
		messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.name) + "s now left in Store")
		instance.save()

		return redirect('/stock_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": 'Issue ' + str(queryset.name),
		"queryset": queryset,
		"form": form,
		"username": 'Issue By: ' + str(request.user),
	}
	return render(request, "add_item.html", context)



def receive_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReceiveForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity += instance.received_quantity
		instance.save()
		messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.name)+"s now in Store")

		return redirect('/stock_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())
	context = {
			"title": 'Reaceive ' + str(queryset.name),
			"instance": queryset,
			"form": form,
			"username": 'Receive By: ' + str(request.user),
		}
	return render(request, "add_item.html", context)


# Create your views here.

