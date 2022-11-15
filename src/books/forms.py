from django import forms
from books import models

class BookGroup(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            'name',
            'logo',
            'price',
            'book_author',
            'book_serie',
            'book_genrie',
            'book_year',
            'book_pages',
            'book_cover',
            'book_format',
            'book_isbn',
            'book_mass',
            'book_age_limits',
            'book_ph',
            'books_in_stock',
            'book_status',
            'book_rating',
            ]