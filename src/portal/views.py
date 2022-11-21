from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class Portal(PermissionRequiredMixin, generic.TemplateView):
    template_name = 'portal/portal.html'
    permission_required = 'auth.view_user', 'referencies.add_publishinghouse', 
    'referencies.add_agelimit', 'referencies.change_rate', 'referencies.delete_publishinghouse',
    'referencies.delete_author', 'referencies.change_author', 'books.change_book', 
    'referencies.change_units', 'referencies.view_units', 'referencies.add_genrie', 
    'referencies.delete_units', 'homepage.add_profile', 'referencies.change_publishinghouse', 
    'referencies.delete_genrie', 'homepage.change_profile', 'referencies.change_serie', 
    'referencies.view_cover', 'referencies.view_rate', 'referencies.delete_cover', 
    'homepage.delete_profile', 'referencies.add_serie', 'referencies.add_rate', 
    'books.view_book', 'referencies.view_agelimit', 'homepage.view_profile', 
    'referencies.view_serie', 'referencies.delete_agelimit', 'referencies.change_agelimit', 
    'referencies.view_author', 'referencies.delete_rate', 'referencies.add_author', 
    'referencies.view_genrie', 'referencies.add_cover', 'referencies.add_units', 
    'referencies.view_publishinghouse', 'books.delete_book', 'referencies.delete_serie', 
    'books.add_book', 'referencies.change_genrie', 'referencies.change_cover'
    #login_url = reverse_lazy('login')
    #redirect_field_name = 'portal'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(self.request.user.get_all_permissions())
        return context