from django.db import models
from core.models import Order

# name, address, active, bottles_ordered


class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    bottles_ordered = models.IntegerField(default=20)


class BottlesCount(models.Model):
    bottle = models.ForeignKey(to=Client, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name="bottle_count")
    count = models.IntegerField(default=1)
    order = models.ForeignKey(to=Order, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name="bottle_count")

    def __str__(self):
        return f"{self.bottle} - {self.count} - {self.order}"

