from django.contrib import admin
from .models import Category, Product,Quantity, Review,Oreder


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Description', 'Price', 'category_relation', 'user_relation', 'created_at')

@admin.register(Quantity)
class Qtyadmin(admin.ModelAdmin):
    list_display=['qty']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_text', 'product_relation', 'user_relation', 'created_at')


@admin.register(Oreder)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product_relation', 'user_relation', 'product_name', 'shipping_address', 'street', 'quantity', 'phone', 'total_price', 'created_at')