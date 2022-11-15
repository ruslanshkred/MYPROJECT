from . import models, forms
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ListBook(LoginRequiredMixin, generic.ListView):
    model = models.Book
    login_url = reverse_lazy('login')
    template_name = 'books/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Books'
        context['url_update_name'] = 'books:book-update'
        context['url_delete_name'] = 'books:book-delete'
        return context

class DetailBook(LoginRequiredMixin, generic.DetailView):
    model = models.Book
    login_url = reverse_lazy('login')
    template_name = 'books/detail.html'

class CreateBook(LoginRequiredMixin, generic.CreateView):
    model = models.Book
    login_url = reverse_lazy('login')
    template_name = 'books/edit.html'
    form_class = forms.BookGroup
    success_url = reverse_lazy('books:book-list')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateBook(LoginRequiredMixin, generic.UpdateView):
    model = models.Book
    login_url = reverse_lazy('login')
    form_class = forms.BookGroup
    template_name = 'books/edit.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteBook(LoginRequiredMixin, generic.DeleteView):
    model = models.Book
    login_url = reverse_lazy('login')
    template_name = 'books/delete.html'
    success_url = reverse_lazy('books:book-list')

