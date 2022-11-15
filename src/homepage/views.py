from django.shortcuts import render
from django.views import generic
from books import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django import forms
from django.views import generic
from django.urls import reverse_lazy

# Create your views here
def user_login(request):
    if request.method == 'GET':
        return render(request, 'homepage/login.html', context={})
    if request.method == 'POST':
        user = authenticate(
            request=request,
            user_name = request.POST.get('login'),
            password = request.POST.get('password')
            )
        if user is not None:
            login(request, user)

class Register(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'homepage/register.html'
    success_url = reverse_lazy('home')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "homepage/signup.html"

class HomePage(generic.TemplateView):
    template_name = 'homepage/home_page.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        atm = models.Book.objects.order_by('-book_input_in_catalog')[0]
        context['photo1'] = models.Book.objects.get(pk=atm.pk)     
        print(atm.pk)
        return context


        