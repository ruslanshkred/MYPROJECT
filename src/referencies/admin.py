from django.contrib import admin

from . import models

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')
class SerieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')
class GenrieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')
class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')
class UnitsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')
class CoverAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')
class AgeLimitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')
class RateAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')

admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Serie, SerieAdmin)
admin.site.register(models.Genrie, GenrieAdmin)
admin.site.register(models.PublishingHouse, PublishingHouseAdmin)
admin.site.register(models.Units, UnitsAdmin)
admin.site.register(models.Cover, CoverAdmin)
admin.site.register(models.AgeLimit, AgeLimitAdmin)
admin.site.register(models.Rate, RateAdmin)