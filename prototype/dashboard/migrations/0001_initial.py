# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
                ('live', models.BooleanField(default=False)),
            ],
        ),
    ]
