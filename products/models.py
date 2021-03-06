from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

LABEL = (
    ('New', 'New'),
    ('Used', 'Used')
)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    item_name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    label = models.CharField(choices=LABEL, max_length=4, default='')
    description = models.TextField()
    slug = models.SlugField(max_length=25, default='')
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Items"

    def __str__(self):
        return self.item_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    #   items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    order_id = models.CharField(max_length=150, null=True)

    class Meta:
        verbose_name_plural = "Order"

    def __str__(self):
        return self.order_id

    @property
    def cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.order_total for item in orderitems])
        return total

    @property
    def cart_total_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    date_added = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "OrderItem"

    def __str__(self):
        return str(self.item)

    @property
    def order_total(self):
        total = self.item.price * self.quantity

        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    postcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
