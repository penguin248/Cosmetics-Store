from django.contrib import admin
from . import models

# Register models
admin.site.register(models.Product)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductImage)
