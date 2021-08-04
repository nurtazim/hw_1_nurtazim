from django.contrib import admin
from product.models import Category
from product.models import Reciew
from product.models import Products
from product.models import Tag

# Register your models here.
admin.site.register(Category)
admin.site.register(Reciew)
admin.site.register(Products)
admin.site.register(Tag)
