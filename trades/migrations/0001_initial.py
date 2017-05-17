# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 15:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_product_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offeredBy', to='products.Product')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivedBy', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentBy', to=settings.AUTH_USER_MODEL)),
                ('wanted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wantedBy', to='products.Product')),
            ],
        ),
    ]
