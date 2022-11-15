from datetime import datetime
from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models



# Create your models here.

class Book(models.Model):
    name = models.CharField(
        max_length = 200,
        verbose_name = 'Title'
    )
    logo = models.ImageField(
        verbose_name = 'Photo',
        upload_to = 'uploads/%Y/%m/%d'
    )
    price = models.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        verbose_name = 'Price, BYN'
    )
    book_author = models.ManyToManyField(
        'referencies.Author',
        verbose_name = 'Authors',
        blank=True,
        related_name='book_authors'
    )

    book_serie = models.ForeignKey(
        'referencies.Serie',
        on_delete = models.PROTECT,
        verbose_name = 'Serie',
    )

    book_genrie = models.ManyToManyField(
        'referencies.Genrie',
        verbose_name = 'Genrie',
        blank=True,
        related_name='book_genriess'
    )

    book_year = models.PositiveIntegerField(
        verbose_name = 'Year of publishing',
    )


    book_pages = models.IntegerField(
        verbose_name = 'Number of pages'
    )

    book_cover = models.ForeignKey(
        'referencies.Cover',
        on_delete = models.PROTECT,
        verbose_name = 'Cover'
    )

    book_format = models.CharField(
        max_length = 100,
        verbose_name = 'Format'
    )
    book_isbn =  models.CharField(
        max_length = 100,
        verbose_name = 'ISBN'
    )
    book_mass = models.IntegerField(
        verbose_name = 'Mass'
    )
    book_age_limits = models.ForeignKey(
        'referencies.AgeLimit',
        on_delete = models.PROTECT,
        verbose_name = 'Age limits'
    )

    book_ph = models.ForeignKey(
        'referencies.PublishingHouse',
        on_delete = models.PROTECT,
        verbose_name = 'Publishing House',
    )

    books_in_stock = models.IntegerField(
        verbose_name = 'Books in Stock'
    )

    book_status = models.BooleanField(
        verbose_name = 'Status'
    )

    book_rating = models.IntegerField(
        verbose_name = 'Rating'
    )

    book_input_in_catalog = models.DateField(
        auto_now_add = True,
        verbose_name='Date of entry into catalogue'
    )

    book_last_change = models.DateField(
        auto_now = True,
        verbose_name='Last changes date'
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name