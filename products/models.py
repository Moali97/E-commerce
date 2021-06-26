from django.conf import settings
from django.db import models

LABEL = (
    ('New', 'New'),
    ('Used', 'Used')
)
#

# This contains the information about each product
class Items(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    label = models.CharField(choices=LABEL, max_length=4, default='')
    description = models.TextField()

    def __str__(self):
        return self.item_name
#maybe add get_add and get_remove

class OrderItem(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"

