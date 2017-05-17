from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profiledetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=False, null=True)
    last_name = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(max_length=200, blank=False, null=True)
    mobile = models.CharField(max_length=30, blank=False, null=True)
    country = models.CharField(max_length=200, blank=False, null=True)
    town = models.CharField(max_length=200, blank=False, null=True)
    address = models.CharField(max_length=200, blank=False, null=True)

    def __str__(self):
        return self.name