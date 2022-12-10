from django.contrib import admin
from . import models
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')
class BookInCartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'book', 'cart', 'quantity', 'price', 'created_date', 'updated_date')
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'cart', 'phone', 'address', 'additional_info', 'created_date', 'updated_date')
class OrderCommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'order',
        'comment',
        'created_date'
        )
admin.site.register(models.OrderComment, OrderCommentAdmin)
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.BookInCart, BookInCartAdmin)
admin.site.register(models.Order, OrderAdmin)