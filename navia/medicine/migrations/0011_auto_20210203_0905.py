# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2021-02-03 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0010_auto_20210203_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinedetail',
            name='sku_name',
            field=models.TextField(db_index=True, max_length=2048),
        ),
    ]