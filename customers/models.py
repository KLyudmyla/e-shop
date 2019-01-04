from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Customers(models.Model):
    user = models.OneToOneField(User, null = True)
    date_of_registration = models.DateField(default=timezone.now)
    contact_details = models.CharField(max_length=55, null=True, blank=True)

    def __str__(self):
        return self.user.username

