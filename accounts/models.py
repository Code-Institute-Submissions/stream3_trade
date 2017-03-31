from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profiledetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    country = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

