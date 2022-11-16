from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Provide a valid email address:')
    first_name = forms.CharField(max_length=100, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=100, required=False, help_text='Optional.')
    phone = forms.IntegerField(help_text='Required. Provide a valid phone number:')
    home_country = forms.CharField(max_length=100, required=False, help_text='Optional.')
    home_city = forms.CharField(max_length=100, required=False, help_text='Optional.')
    home_index = forms.CharField(max_length=100, required=False, help_text='Optional.')
    home_address1 = forms.CharField(max_length=100, required=False, help_text='Optional.')
    home_address2 = forms.CharField(max_length=100, required=False, help_text='Optional.')
    additional_info = forms.CharField(max_length=500, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email", "first_name", "last_name", 
            "phone", "home_country", "home_city", "home_index", "home_address1", "home_address2",
            "additional_info"]

