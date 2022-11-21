from django.contrib import admin
from . import models
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'phone',
        'home_country',
        'home_city',
        'home_index',
        'home_address1',
        'home_address2',
        'additional_info'
        )

admin.site.register(models.Profile, ProfileAdmin)