from datetime import datetime
from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models



# Create your models here.

class Book(models.Model):
    name = models.CharField(
        max_length = 200,
        verbose_name = 'Название книги'
    )
    logo = models.ImageField(
        verbose_name = 'Фото обложки',
        upload_to = 'uploads/%Y/%m/%d'
    )
    price = models.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        verbose_name = 'Цена, BYN'
    )
    book_author = models.ManyToManyField(
        'referencies.Author',
        verbose_name = 'Авторы',
        blank=True,
        related_name='book_authors'
    )

    book_serie = models.ForeignKey(
        'referencies.Serie',
        on_delete = models.PROTECT,
        verbose_name = 'Серия',
    )

    book_genrie = models.ManyToManyField(
        'referencies.Genrie',
        verbose_name = 'Жанры',
        blank=True,
        related_name='book_genriess'
    )

    book_year = models.DateField(
        verbose_name = 'Год издания',
    )

    book_pages = models.IntegerField(
        verbose_name = 'Страницы'
    )

    book_cover = models.ForeignKey(
        'referencies.Cover',
        on_delete = models.PROTECT,
        verbose_name = 'Переплет'
    )

    book_format = models.CharField(
        max_length = 100,
        verbose_name = 'Формат'
    )
    book_isbn =  models.CharField(
        max_length = 100,
        verbose_name = 'ISBN'
    )
    book_mass = models.IntegerField(
        verbose_name = 'Вес'
    )
    book_age_limits = models.ForeignKey(
        'referencies.AgeLimit',
        on_delete = models.PROTECT,
        verbose_name = 'Возрастные ограничения'
    )

    book_ph = models.ForeignKey(
        'referencies.PublishingHouse',
        on_delete = models.PROTECT,
        verbose_name = 'Издательство',
    )

    books_in_stock = models.IntegerField(
        verbose_name = 'Вес'
    )

    book_status = models.BooleanField(
        verbose_name = 'Статус'
    )

    book_rating = models.IntegerField(
        verbose_name = 'Рейтинг'
    )

    book_input_in_catalog = models.DateField(
        verbose_name='Дата внесения в каталог'
    )

    book_last_change = models.DateField(
        verbose_name='Дата последнего изменения'
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name