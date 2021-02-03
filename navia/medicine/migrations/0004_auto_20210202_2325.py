# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2021-02-02 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_auto_20210202_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinedetail',
            name='manufacturer_name',
            field=models.CharField(db_index=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name='medicinedetail',
            name='salt_name',
            field=models.CharField(db_index=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name='medicinedetail',
            name='sku_name',
            field=models.CharField(db_index=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name='medicinedetail',
            name='strength',
            field=models.CharField(db_index=True, max_length=1024),
        ),
    ]