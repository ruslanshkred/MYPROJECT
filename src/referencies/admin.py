from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Author)
admin.site.register(models.Serie)
admin.site.register(models.Genrie)
admin.site.register(models.PublishingHouse)
admin.site.register(models.Units)