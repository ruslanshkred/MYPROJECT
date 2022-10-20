from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(
        max_length = 40,
        verbose_name = 'Author name'
    )
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return f'/author/{self.pk}'


class Serie(models.Model):
    name = models.CharField(
        max_length = 30,
        verbose_name = "Serie name"
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return f'/author/{self.pk}'


class Genrie(models.Model):
    name = models.CharField(
        max_length = 30,
        verbose_name = "Genrie name"
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/author/{self.pk}'


class PublishingHouse(models.Model):
    name = models.CharField(
        max_length = 50,
        verbose_name = "Publishing House name"
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return f'/author/{self.pk}'


class Units(models.Model):
    name = models.CharField(
        max_length = 10,
        verbose_name = "Units name"
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
        
    def get_absolute_url(self):
        return f'/author/{self.pk}'