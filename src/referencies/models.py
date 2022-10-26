from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse_lazy
# Create your models here.

class Author(models.Model):
    name = models.CharField(
        max_length = 40,
        verbose_name = 'Имя автора'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('author-list', kwargs={'pk': self.pk})


class Serie(models.Model):
    name = models.CharField(
        max_length = 30,
        verbose_name = "Серия"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name = 'Описание'
    )
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('serie-list', kwargs={'pk': self.pk})


class Genrie(models.Model):
    name = models.CharField(
        max_length = 30,
        verbose_name = "Жанр"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name = 'Описание'
    )
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('genrie-list', kwargs={'pk': self.pk})


class PublishingHouse(models.Model):
    name = models.CharField(
        max_length = 50,
        verbose_name = "Издательство"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name = 'Описание'
    )
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('ph-list', kwargs={'pk': self.pk})


class Units(models.Model):
    name = models.CharField(
        max_length = 10,
        verbose_name = "Единицы измерения"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name = 'Описание'
    )
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse_lazy('author-list', kwargs={'units': self.pk})

class Cover(models.Model):
    name = models.CharField(
        max_length = 50,
        verbose_name = "Переплет"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name = 'Описание'
    )
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('cover-list', kwargs={'pk': self.pk})

class AgeLimit(models.Model):
    name = models.CharField(
        max_length = 10,
        verbose_name = "Возрастные ограничения"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name = 'Описание'
    )
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('al-list', kwargs={'pk': self.pk})

class Rate(models.Model):
    name = models.CharField(
        max_length = 10,
        verbose_name = "Рейтинг"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name = 'Описание'
    )
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('rate-list', kwargs={'pk': self.pk})