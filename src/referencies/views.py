from . import models, forms
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

class ListAuthor(PermissionRequiredMixin, generic.ListView):
    model = models.Author
    permission_required = 'referencies.view_author'
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Authors'
        context['url_update_name'] = 'referencies:author-update'
        context['url_delete_name'] = 'referencies:author-delete'
        context['url_create_name'] = 'referencies:author-create'
        context['operation_for_add'] = 'Add new Author'
        return context

class DetailAuthor(PermissionRequiredMixin, generic.DetailView):
    model = models.Author
    permission_required = 'referencies.view_author'
    template_name = 'referencies/detail.html'

class CreateAuthor(PermissionRequiredMixin, generic.CreateView):
    model = models.Author
    permission_required = 'referencies.add_author'
    form_class = forms.AuthorGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:author-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateAuthor(PermissionRequiredMixin, generic.UpdateView):
    model = models.Author
    permission_required = 'referencies.change_author',
    form_class = forms.AuthorGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:author-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context
    
class DeleteAuthor(PermissionRequiredMixin, generic.DeleteView):
    model = models.Author
    permission_required = 'referencies.delete_author'
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:author-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Delete'
        return context


class ListSerie(PermissionRequiredMixin, generic.ListView):
    model = models.Serie
    permission_required = 'referencies.view_serie'
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Series'
        context['url_update_name'] = 'referencies:serie-update'
        context['url_delete_name'] = 'referencies:serie-delete'
        context['url_create_name'] = 'referencies:serie-create'
        context['operation_for_add'] = 'Add new Serie'
        return context

class DetailSerie(PermissionRequiredMixin, generic.DetailView):
    model = models.Serie
    permission_required = 'referencies.view_serie'
    template_name = 'referencies/detail.html'

class CreateSerie(PermissionRequiredMixin, generic.CreateView):
    model = models.Serie
    permission_required = 'referencies.add_serie'
    form_class = forms.SerieGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:serie-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateSerie(PermissionRequiredMixin, generic.UpdateView):
    model = models.Serie
    permission_required = 'referencies.change_serie'
    form_class = forms.SerieGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:serie-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteSerie(PermissionRequiredMixin, generic.DeleteView):
    model = models.Serie
    permission_required = 'referencies.delete_serie'
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:serie-list')


class ListGenrie(PermissionRequiredMixin, generic.ListView):
    model = models.Genrie
    permission_required = 'referencies.view_genrie'
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Genries'
        context['url_update_name'] = 'referencies:genrie-update'
        context['url_delete_name'] = 'referencies:genrie-delete'
        context['url_create_name'] = 'referencies:genrie-create'
        context['operation_for_add'] = 'Add new Genrie'
        return context

class DetailGenrie(PermissionRequiredMixin, generic.DetailView):
    model = models.Genrie
    permission_required = 'referencies.view_genrie'
    template_name = 'referencies/detail.html'

class CreateGenrie(PermissionRequiredMixin, generic.CreateView):
    model = models.Genrie
    permission_required = 'referencies.add_genrie'
    form_class = forms.GenrieGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:genrie-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateGenrie(PermissionRequiredMixin, generic.UpdateView):
    model = models.Genrie
    permission_required = 'referencies.change_genrie'
    form_class = forms.GenrieGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:genrie-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteGenrie(PermissionRequiredMixin, generic.DeleteView):
    model = models.Genrie
    permission_required = 'referencies.delete_genrie'
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:genrie-list')



class ListPublishingHouse(PermissionRequiredMixin, generic.ListView):
    model = models.PublishingHouse
    permission_required = 'referencies.view_publishinghouse'
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Publishing Houses'
        context['url_update_name'] = 'referencies:ph-update'
        context['url_delete_name'] = 'referencies:ph-delete'
        context['url_create_name'] = 'referencies:ph-create'
        context['operation_for_add'] = 'Add new Publishing House'
        return context

class DetailPublishingHouse(PermissionRequiredMixin, generic.DetailView):
    model = models.PublishingHouse
    permission_required = 'referencies.view_publishinghouse'
    template_name = 'referencies/detail.html'

class CreatePublishingHouse(PermissionRequiredMixin, generic.CreateView):
    model = models.PublishingHouse
    permission_required = 'referencies.add_publishinghouse'
    form_class = forms.PublishingHouseGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:ph-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdatePublishingHouse(PermissionRequiredMixin, generic.UpdateView):
    model = models.PublishingHouse
    permission_required = 'referencies.change_publishinghouse'
    form_class = forms.PublishingHouseGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:ph-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeletePublishingHouse(PermissionRequiredMixin, generic.DeleteView):
    model = models.PublishingHouse
    permission_required = 'referencies.delete_publishinghouse'
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:ph-list')



class ListUnits(PermissionRequiredMixin, generic.ListView):
    model = models.Units
    permission_required = 'referencies.view_units'
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Units'
        context['url_update_name'] = 'referencies:units-update'
        context['url_delete_name'] = 'referencies:units-delete'
        context['url_create_name'] = 'referencies:units-create'
        context['operation_for_add'] = 'Add new Units'
        return context

class DetailUnits(PermissionRequiredMixin, generic.DetailView):
    model = models.Units
    permission_required = 'referencies.view_units'
    template_name = 'referencies/detail.html'

class CreateUnits(PermissionRequiredMixin, generic.CreateView):
    model = models.Units
    permission_required = 'referencies.add_units'
    form_class = forms.UnitsGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:units-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateUnits(PermissionRequiredMixin, generic.UpdateView):
    model = models.Units
    permission_required = 'referencies.change_units'
    form_class = forms.UnitsGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:units-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteUnits(PermissionRequiredMixin, generic.DeleteView):
    model = models.Units
    permission_required = 'referencies.delete_units'
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:units-list')


class ListCover(PermissionRequiredMixin, generic.ListView):
    model = models.Cover
    permission_required = 'referencies.view_cover'
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Covers'
        context['url_update_name'] = 'referencies:cover-update'
        context['url_delete_name'] = 'referencies:cover-delete'
        context['url_create_name'] = 'referencies:cover-create'
        context['operation_for_add'] = 'Add new Cover'
        return context

class DetailCover(PermissionRequiredMixin, generic.DetailView):
    model = models.Cover
    permission_required = 'referencies.view_cover'
    template_name = 'referencies/detail.html'

class CreateCover(PermissionRequiredMixin, generic.CreateView):
    model = models.Cover
    permission_required = 'referencies.add_cover'
    form_class = forms.CoverGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:cover-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateCover(PermissionRequiredMixin, generic.UpdateView):
    model = models.Cover
    permission_required = 'referencies.change_cover'
    form_class = forms.CoverGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:cover-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteCover(PermissionRequiredMixin, generic.DeleteView):
    model = models.Cover
    permission_required = 'referencies.delete_cover'
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:cover-list')


class ListAgeLimit(PermissionRequiredMixin, generic.ListView):
    model = models.AgeLimit
    permission_required = 'referencies.view_agelimit'
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Age Limits'
        context['url_update_name'] = 'referencies:al-update'
        context['url_delete_name'] = 'referencies:al-delete'
        context['url_create_name'] = 'referencies:al-create'
        context['operation_for_add'] = 'Add new Age Limit'
        return context

class DetailAgeLimit(PermissionRequiredMixin, generic.DetailView):
    model = models.AgeLimit
    permission_required = 'referencies.view_agelimit'
    template_name = 'referencies/detail.html'

class CreateAgeLimit(PermissionRequiredMixin, generic.CreateView):
    model = models.AgeLimit
    permission_required = 'referencies.create_agelimit'
    form_class = forms.AgeLimitGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:al-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateAgeLimit(PermissionRequiredMixin, generic.UpdateView):
    model = models.AgeLimit
    permission_required = 'referencies.change_agelimit'
    form_class = forms.AgeLimitGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:al-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteAgeLimit(PermissionRequiredMixin, generic.DeleteView):
    model = models.AgeLimit
    permission_required = 'referencies.delete_agelimit'
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:al-list')



class ListRate(PermissionRequiredMixin, generic.ListView):
    model = models.Rate
    permission_required = 'referencies.view_rate'
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Rates'
        context['url_update_name'] = 'referencies:rate-update'
        context['url_delete_name'] = 'referencies:rate-delete'
        context['url_create_name'] = 'referencies:rate-create'
        context['operation_for_add'] = 'Add new Rate'
        return context

class DetailRate(PermissionRequiredMixin, generic.DetailView):
    model = models.Rate
    permission_required = 'referencies.view_rate'
    template_name = 'referencies/detail.html'

class CreateRate(PermissionRequiredMixin, generic.CreateView):
    model = models.Rate
    permission_required = 'referencies.add_rate'
    form_class = forms.RateGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:rate-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateRate(PermissionRequiredMixin, generic.UpdateView):
    model = models.Rate
    permission_required = 'referencies.change_rate'
    form_class = forms.RateGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:rate-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteRate(PermissionRequiredMixin, generic.DeleteView):
    model = models.Rate
    permission_required = 'referencies.delete_rate'
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:rate-list')