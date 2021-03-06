# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reports', '0002_auto_20170319_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retailer_file', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='')),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
