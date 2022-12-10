from datetime import datetime
from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



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
    book_author = models.ForeignKey(
        'referencies.Author',
        verbose_name = 'Author',
        default=1,
        related_name='books',
        on_delete=models.PROTECT
    )

    book_serie = models.ForeignKey(
        'referencies.Serie',
        on_delete = models.PROTECT,
        verbose_name = 'Serie',
        related_name='books'
    )

    book_genrie = models.ForeignKey(
        'referencies.Genrie',
        verbose_name = 'Genrie',
        on_delete=models.PROTECT,
        default=1,
        related_name='books',
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
        related_name='books',
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

class BookComment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='book_comment',
        verbose_name="Comment of the user"
    )
    book = models.ForeignKey(
        'books.Book',
        verbose_name = 'Book to comment',
        related_name='book_comment',
        on_delete = models.PROTECT
    )
    comment = models.TextField(
        verbose_name= 'Comment'
    )
    created_date = models.DateTimeField(
        verbose_name = 'Created date',
        auto_now = False,
        auto_now_add = True
    )
    def __str__(self):
        return self.comment
