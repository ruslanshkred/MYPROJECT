from django import forms
from referencies import models


class AuthorGroup(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ['name', 'description']

class SerieGroup(forms.ModelForm):
    class Meta:
        model = models.Serie
        fields = ['name', 'description']

class GenrieGroup(forms.ModelForm):
    class Meta:
        model = models.Genrie
        fields = ['name', 'description']

class PublishingHouseGroup(forms.ModelForm):
    class Meta:
        model = models.PublishingHouse
        fields = ['name', 'description']


class UnitsGroup(forms.ModelForm):
    class Meta:
        model = models.Units
        fields = ['name', 'description']

class CoverGroup(forms.ModelForm):
    class Meta:
        model = models.Cover
        fields = ['name', 'description']


class AgeLimitGroup(forms.ModelForm):
    class Meta:
        model = models.AgeLimit
        fields = ['name', 'description']

class RateGroup(forms.ModelForm):
    class Meta:
        model = models.Rate
        fields = ['name', 'description']

class StatusGroup(forms.ModelForm):
    class Meta:
        model = models.Status
        fields = ['name', 'description']