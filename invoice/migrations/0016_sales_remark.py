# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-01-26 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0015_sales_mixcardamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='remark',
            field=models.CharField(default='N/A', max_length=300),
        ),
    ]