from django.conf import settings
from django.db import models
from django.shortcuts import reverse

LABEL = (
    ('New', 'New'),
    ('Used', 'Used')
)


# This contains the information about each product
class Items(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    label = models.CharField(choices=LABEL, max_length=4, default='')
    description = models.TextField()
    slug = models.SlugField( default='')

    class Meta:
        verbose_name_plural = "Items"

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("products:product", kwargs={
            "slug" : self.slug
        })


# maybe add get_add and get_remove

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "OrderItem"

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Order"

    def __str__(self):
        return self.user.username
