# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-02-17 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mamtaApp', '0012_moneycollection_companyid'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashMoneyCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('remark', models.CharField(blank=True, max_length=500, null=True)),
                ('message', models.CharField(blank=True, max_length=500, null=True)),
                ('paymentMode', models.CharField(default='Cash', max_length=100)),
                ('chequeImage', models.ImageField(blank=True, null=True, upload_to='Cheques')),
                ('latitude', models.CharField(default='0.0', max_length=200)),
                ('longitude', models.CharField(default='0.0', max_length=200)),
                ('isDeleted', models.BooleanField(default=False)),
                ('isAddedInSales', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('buyerID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mamtaApp.Buyer')),
                ('collectedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mamtaApp.StaffUser')),
                ('companyID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mamtaApp.Company')),
            ],
        ),
    ]