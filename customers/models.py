# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.TextField(max_length=100)
    class Meta:
		app_label = 'customer_data'