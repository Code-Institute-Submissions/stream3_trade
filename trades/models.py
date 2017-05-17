from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from products.models import Product


class Trades(models.Model):
    sender = models.ForeignKey(User, related_name='sentBy')
    receiver = models.ForeignKey(User, related_name='receivedBy')
    wanted = models.ForeignKey(Product, related_name='wantedBy')
    offered = models.ForeignKey(Product, related_name='offeredBy')
# Create your models here.
