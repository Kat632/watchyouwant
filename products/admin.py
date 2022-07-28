from django.contrib import admin
from .models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    """
    class to enable admin to manage product model
    """
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
    """
    class to enable admin to manage category model
    """
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    class to enable admin to  manage user model
    """
    list_display = (
        'product',
        'user',
        'review_time',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
