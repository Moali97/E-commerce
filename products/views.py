from django.shortcuts import render
from .models import *
from django.http import JsonResponse

def store(request):
    items = Item.objects.all()
    context = {'items':items}

    return render(request, 'store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, ordered=False)
        orders = order.orderitem_set.all()
    else:
        orders = []
        order = {'cart_total':0, 'cart_total_items':0}

    context = {'orders':orders,
               'order':order
               }

    return render(request, 'cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, ordered=False)
        orders = order.orderitem_set.all()
    else:
        orders = []
        order = {'cart_total': 0, 'cart_total_items': 0}

    context = {'orders': orders,
               'order': order
               }
    return render(request, 'checkout.html', context)


def updateItem(request):
    return JsonResponse('Item added to your cart', safe=False)