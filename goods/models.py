
from django.db import models
from customers.models import Customers
from staff.models import Staff
from django.utils import timezone


class Good(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Discount_code(models.Model):
    code = models.CharField(max_length=7)
    good = models.ForeignKey(Good)
    customer = models.ForeignKey(Customers)
    staff = models.ForeignKey(Staff)
    date_of_issue = models.DateField(default=timezone.now)

    def __str__(self):
        return self.code