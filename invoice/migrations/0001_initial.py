# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-08-27 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mamtaApp', '0006_auto_20190725_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceSerial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serials', models.IntegerField(default=1)),
                ('isDeleted', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.IntegerField(default=1)),
                ('isDeleted', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('assignedTo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mamtaApp.StaffUser')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('salesType', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('isCash', models.BooleanField(default=True)),
                ('customerName', models.CharField(blank=True, max_length=200, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mamtaApp.StaffUser')),
                ('invoiceSerialID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.InvoiceSerial')),
            ],
        ),
        migrations.AddField(
            model_name='invoiceserial',
            name='invoiceSeriesID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.InvoiceSeries'),
        ),
    ]
