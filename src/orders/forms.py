from django import forms
from . import models


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['phone', 'address', 'additional_info']

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['status', 'phone', 'address', 'additional_info']

class BookInCartForm(forms.ModelForm):
    class Meta:
        model = models.BookInCart
        fields = ['book', 'quantity']


class OrderCommentForm(forms.ModelForm):
    class Meta:
        model = models.OrderComment
        fields = ['comment']