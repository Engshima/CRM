from ast import Return
from multiprocessing import context
from telnetlib import STATUS
from xml.dom import INVALID_STATE_ERR
from django.shortcuts import render
from django.http import HttpResponse
from .forms import OrderForm
from django.shortcuts import redirect


# create your views here.
from .models import *
from .models import customer as customerr
from django.forms import inlineformset_factory
from django.db.models.signals import post_migrate
from .filters import OrderFilter

def home(request):
    orders = order.objects.all()
    Customers = customerr.objects.all()
    total_Customers = Customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='delivered').count
    pending = orders.filter(status='pending').count
    context = {'orders': orders, 'Customers': Customers, 'total_Customers': total_Customers,
               'total_orders': total_orders, 'delivered': delivered, 'pending': pending, }

    return render(request, 'account/dashboard.html', context)


def product(request):
    return render(request, 'account/product.html')


def customer(request, pk_test):
    customer = customerr.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    Myfilter = OrderFilter(request.GET,queryset = orders)
    orders = Myfilter.qs
    context = {'customer': customer,
               'orders': orders, 'order_count': order_count,'Myfilter':Myfilter}
    return render(request, 'account/customer.html', context)


def CreateOrder(request, pk):
    OrderFormset = inlineformset_factory(customerr, order, fields=('product','status'), extra=10)
    customer = customerr.objects.get(id=pk)
    formset = OrderFormset(instance=customer)
    if request.method == 'POST':
        formset = OrderFormset(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
             
    context = {'form': formset}
    return render(request, 'account/order_form.html', context)


def UpdateOrder(request, pk):
    Order = order.objects.get(id=pk)
    form = OrderForm(instance=Order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=Order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'account/order_form.html', context)


def DeleteOrder(request, pk):
    Order = order.objects.get(id=pk)
    if request.method == 'POST':
        Order.delete()
        return redirect('/')
    context = {'item': Order}
    return render(request, 'account/delete.html', context)
