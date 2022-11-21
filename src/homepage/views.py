from django.shortcuts import render
from django.views import generic
from books import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse_lazy
from . import forms
from . import models as profile_models
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here
#def user_login(request):
#    if request.method == 'GET':
#        return render(request, 'homepage/login.html', context={})
 #   if request.method == 'POST':
 #       user = authenticate(
 #           request=request,
 #           user_name = request.POST.get('login'),
 #           password = request.POST.get('password')
 #           )
  #      if user is not None:
 #           login(request, user)

class Profile(LoginRequiredMixin, generic.CreateView):
    form_class = forms.ProfileForm
    login_url = reverse_lazy('login')
    
    template_name = 'homepage/profile_create.html'
    success_url = reverse_lazy('home_page')

class ListProfile(LoginRequiredMixin, generic.ListView):
    model = profile_models.Profile
    login_url = reverse_lazy('login')
    template_name = 'homepage/profile_list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Profiles'
        context['url_update_name'] = 'homepage:profile-update'
        context['url_delete_name'] = 'homepage:profile-delete'
        return context

class DetailProfile(LoginRequiredMixin, generic.DetailView):
    model = profile_models.Profile
    login_url = reverse_lazy('login') 
    template_name = 'homepage/profile_detail.html'

class UpdateProfile(LoginRequiredMixin, generic.UpdateView):
    model = profile_models.Profile
    login_url = reverse_lazy('login')
    form_class = forms.ProfileForm
    template_name = 'homepage/profile_edit.html'
    success_url = reverse_lazy('homepage:profile-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteProfile(LoginRequiredMixin, generic.DeleteView):
    model = profile_models.Profile
    login_url = reverse_lazy('login')
    template_name = 'homepage/profile_delete.html'
    success_url = reverse_lazy('homepage:profile-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Delete'
        return context


class SignUp(generic.CreateView):
    form_class = forms.RegisterForm
    success_url = reverse_lazy('homepage:profile-create')
    template_name = "homepage/signup.html"




class HomePage(generic.TemplateView):
    template_name = 'homepage/home_page.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        for i in range(5):
            atm = models.Book.objects.order_by('-book_input_in_catalog')[i]
            context[f'photo{i+1}'] = models.Book.objects.get(pk=atm.pk)
        return context

class Delivery(generic.TemplateView):
    template_name = 'homepage/delivery.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Terms of Delivery'
        return context
        