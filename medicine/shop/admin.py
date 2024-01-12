from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ('heading', 'category', 'date')

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'producer', 'price', 'quantity', 'recipe_required', 'in_stock')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'feedback', 'stars')

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'date_created', 'total_price')

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1
