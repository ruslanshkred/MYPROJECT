from . import models, forms
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

class ListBook(generic.ListView):
    model = models.Book
    template_name = 'books/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Books'
        context['url_update_name'] = 'books:book-update'
        context['url_delete_name'] = 'books:book-delete'
        context['url_create_name'] = 'books:book-create'
        context['url_detail_name'] = 'books:book-detail'
        context['operation_for_add'] = 'Add new Book'
        return context

class DetailBook(generic.DetailView):
    model = models.Book
    template_name = 'books/detail.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['photo'] = id
        context['url_detail_name'] = 'books:book-detail'
        return context

class CreateBook(PermissionRequiredMixin, generic.CreateView):
    model = models.Book
    permission_required = 'books.add_book'
    template_name = 'books/edit.html'
    form_class = forms.BookGroup
    success_url = reverse_lazy('books:book-list')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateBook(PermissionRequiredMixin, generic.UpdateView):
    model = models.Book
    permission_required = 'books.change_book'
    form_class = forms.BookGroup
    template_name = 'books/edit.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteBook(PermissionRequiredMixin, generic.DeleteView):
    model = models.Book
    permission_required = 'books.delete_book'
    template_name = 'books/delete.html'
    success_url = reverse_lazy('books:book-list')

