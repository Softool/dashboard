from django.shortcuts import render, redirect
from .models import Product, Customer, Order
from .forms import Orderform, Customerform


# Create your views here.
def dashboard(request):
    orders = Order.objects.all()
    cust = Customer.objects.all()
    total_order = orders.count()
    deliver = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out = orders.filter(status='Out for delivery').count()


    context = {
        'orders': orders,
        'cust': cust,
        'total_order': total_order,
        'deliver': deliver,
        'pending': pending,
        'out': out,
    }
    return render(request, 'dashapp/dashboard.html', context)


def product(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, 'dashapp/product.html', context)


def customer(request, pk_test):
    cust = Customer.objects.get(id=pk_test)
    order = cust.order_set.all()
    order_count = order.count()
    context = {
        'pk_test': pk_test,
        'cust': cust,
        'order': order,
        'order_count': order_count
    }
    return render(request, 'dashapp/customer.html', context)


def createOrder(request):
    form = Orderform()
    if request.method == 'POST':
        form = Orderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'dashapp/order_create.html', context)


def createCustomer(request):
    form = Customerform()
    if request.method == 'POST':
        form = Customerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = Customerform()
    context = {'form': form}
    return render(request, 'dashapp/customer_create.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = Orderform(instance=order)
    if request.method == 'POST':
        form = Orderform(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'dashapp/order_create.html', context)




def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = Orderform(instance=order)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'order': order
    }
    return render(request, 'dashapp/delete.html', context)


