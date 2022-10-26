from django.contrib import admin

from . import models

# Register your models here.



class BookAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'logo',
        'price',
        #'book_author',
        #'book_genrie',
        'book_year',
        'book_pages',
        'book_cover',
        'book_format',
        'book_isbn',
        'book_mass',
        'book_ph',
        'books_in_stock',
        'book_status',
        'book_rating',
        'book_input_in_catalog',
        'book_last_change'
        )

admin.site.register(models.Book, BookAdmin)