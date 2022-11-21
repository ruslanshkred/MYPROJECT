from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from homepage import models

class RegisterForm(UserCreationForm):
     email = forms.EmailField(max_length=254, help_text='Required. Provide a valid email address:')
     class Meta:
         model = User
         fields = ["username", "password1", "password2", "email"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = [
            "user",
            "phone",
            "home_country",
            "home_city",
            "home_index",
            "home_address1",
            "home_address2",
            "additional_info"]


