# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-02-09 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0019_openingandclosingbalance_createdby'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesEdit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amountBefore', models.FloatField(default=0.0)),
                ('amountAfter', models.FloatField(default=0.0)),
                ('remark', models.CharField(default='N/A', max_length=300)),
                ('isDeleted', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('salesID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.Sales')),
            ],
        ),
    ]
