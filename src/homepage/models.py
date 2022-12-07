from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.PROTECT,
        verbose_name="Group",
        default=2
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name='First name',
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Last name'
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
        return self.user.first_name

    def get_absolute_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = 'Profile'


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()