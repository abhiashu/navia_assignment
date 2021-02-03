# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class medicineDetail(models.Model):
    id = models.AutoField(primary_key=True)
    sku_id = models.IntegerField(null=True, blank=True)
    product_id = models.IntegerField(null=True, blank=True)
    sku_name = models.TextField(max_length=2048, null=False, blank=False, db_index=True)
    price = models.FloatField()
    manufacturer_name = models.CharField(max_length=2048, db_index=True, null=True, blank=True)
    salt_name = models.CharField(max_length=2048, db_index=True, null=True, blank=True)
    drug_form = models.CharField(max_length=2048, null=True, blank=True)
    pack_size = models.CharField(max_length=2048, null=True, blank=True)
    strength = models.CharField(max_length=1024, db_index=True, null=True, blank=True)
    product_banned_flag = models.NullBooleanField(null=True, blank=True)
    unit = models.CharField(max_length=255, null=True, blank=True)
    price_per_unit = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.product_id)

    # class Meta:
    #     managed = False
    #     db_table = 'medicine_medicinedetail'





