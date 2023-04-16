from django.contrib import admin
from .models import Category, Product, Brand, ProductLine

# Register your models here.


class ProductLineAdmin(admin.TabularInline):
    model = ProductLine


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductLineAdmin,
    ]


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductLine)
