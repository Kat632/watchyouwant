from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'brand',
        'colour',
        'stock_level',
        'price',
        'rating',
        'image',
        'movement_origin',
        'movement_type',
        'water_resistance',
        'weight',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin class for Review model
    With list_display to show fields
    to user
    """
    list_display = (
        'product',
        'user',
        'review_time',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
