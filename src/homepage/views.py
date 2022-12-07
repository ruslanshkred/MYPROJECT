from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from books import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User, Group
from django import forms
from django.urls import reverse_lazy
from . import forms
from . import models as profile_models
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.db.models import Q


class Profile(LoginRequiredMixin, generic.CreateView):
    form_class = forms.ProfileForm
    login_url = reverse_lazy('login')
    template_name = 'homepage/profile_create.html'
    success_url = reverse_lazy('home_page')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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
    def get_object(self):
        return self.request.user.profile


class UpdateProfile(LoginRequiredMixin, generic.UpdateView):
    model = profile_models.Profile
    login_url = reverse_lazy('login')
    form_class = forms.ProfileForm
    template_name = 'homepage/profile_edit.html'
    success_url = reverse_lazy('home_page')

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
    def form_valid(self, form):
        user = form.save()
        user_group = Group.objects.get(name='customers')
        user.groups.add(user_group)
        login(self.request, user)
        return redirect(self.success_url)


class HomePage(generic.TemplateView):
    template_name = 'homepage/home_page.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['five_lasts'] = models.Book.objects.order_by('-book_input_in_catalog').all()[:4]
        return context

class Delivery(generic.TemplateView):
    template_name = 'homepage/delivery.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Terms of Delivery'
        return context


class SearchResultsView(generic.ListView):
    model = models.Book
    template_name = 'homepage/search.html'
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        queryset = models.Book.objects.filter(
            Q(name__icontains=query) | Q(book_author__name__icontains=query) |
            Q(book_serie__name__icontains=query) | Q(book_genrie__name__icontains=query)
        )
        print(query)
        return queryset