# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, null=False)
    parentCategory = models.ForeignKey("Category", null=True, related_name='parent')


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    category = models.ForeignKey(Category, default='', on_delete=models.CASCADE, related_name='category')
    subCategory = models.ForeignKey(Category, default='', on_delete=models.CASCADE, related_name='subCategory')
