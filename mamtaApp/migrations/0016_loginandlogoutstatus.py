# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-08-01 19:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mamtaApp', '0015_suppliercollection_isapproved'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginAndLogoutStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusType', models.CharField(blank=True, max_length=100, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('companyID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mamtaApp.Company')),
                ('userID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
