from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    phone = models.PositiveIntegerField(
        verbose_name='Phone number'
    )
    home_country = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Home country'
    )
    home_city = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Home city'
    )
    home_index = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Home index'
    )
    home_address1 = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Home address1'
    )
    home_address2 = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Home address2'
    )
    additional_info = models.TextField(
        blank=True,
        null=True,
        verbose_name = 'Additional info'
    )
    def __str__(self):
        return self.user.username

    def __repr__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.pk})