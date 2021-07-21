from django.shortcuts import render
from .models import Item


def store(request):
    items = Item.objects.all()
    context = {'items':items}

    return render(request, 'store.html', context)


def cart(request):
    context = {}
    return render(request, 'cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)