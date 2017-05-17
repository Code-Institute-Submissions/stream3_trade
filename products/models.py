from __future__ import unicode_literals

from django.contrib.auth.models import User


from django.db import models


class Product(models.Model):
    owner = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(upload_to='images', blank=True)


    def __str__(self):
        return self.name