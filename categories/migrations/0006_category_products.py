# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_category'),
        ('categories', '0005_remove_category_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]