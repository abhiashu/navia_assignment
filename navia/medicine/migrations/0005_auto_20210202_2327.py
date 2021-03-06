# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2021-02-02 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0004_auto_20210202_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinedetail',
            name='drug_form',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='medicinedetail',
            name='pack_size',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='medicinedetail',
            name='product_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicinedetail',
            name='salt_name',
            field=models.CharField(blank=True, db_index=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='medicinedetail',
            name='sku_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicinedetail',
            name='strength',
            field=models.CharField(blank=True, db_index=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='medicinedetail',
            name='unit',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
