# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Category, Product
from django.contrib import admin


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
