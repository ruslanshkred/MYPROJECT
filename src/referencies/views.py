from . import models, forms
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ListAuthor(LoginRequiredMixin, generic.ListView):
    model = models.Author
    login_url = reverse_lazy('login')
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Authors'
        context['url_update_name'] = 'referencies:author-update'
        context['url_delete_name'] = 'referencies:author-delete'
        return context

class DetailAuthor(LoginRequiredMixin, generic.DetailView):
    model = models.Author
    login_url = reverse_lazy('login') 
    template_name = 'referencies/detail.html'

class CreateAuthor(LoginRequiredMixin, generic.CreateView):
    model = models.Author
    login_url = reverse_lazy('login')
    form_class = forms.AuthorGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:author-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateAuthor(LoginRequiredMixin, generic.UpdateView):
    model = models.Author
    login_url = reverse_lazy('login')
    form_class = forms.AuthorGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:author-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context
    
class DeleteAuthor(LoginRequiredMixin, generic.DeleteView):
    model = models.Author
    login_url = reverse_lazy('login')
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:author-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Delete'
        return context


class ListSerie(LoginRequiredMixin, generic.ListView):
    model = models.Serie
    login_url = reverse_lazy('login')
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Series'
        context['url_update_name'] = 'referencies:serie-update'
        context['url_delete_name'] = 'referencies:serie-delete'
        return context

class DetailSerie(LoginRequiredMixin, generic.DetailView):
    model = models.Serie
    login_url = reverse_lazy('login')
    template_name = 'referencies/detail.html'

class CreateSerie(LoginRequiredMixin, generic.CreateView):
    model = models.Serie
    login_url = reverse_lazy('login')
    form_class = forms.SerieGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:serie-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateSerie(LoginRequiredMixin, generic.UpdateView):
    model = models.Serie
    login_url = reverse_lazy('login')
    form_class = forms.SerieGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:serie-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteSerie(LoginRequiredMixin, generic.DeleteView):
    model = models.Serie
    login_url = reverse_lazy('login')
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:serie-list')


class ListGenrie(LoginRequiredMixin, generic.ListView):
    model = models.Genrie
    login_url = reverse_lazy('login')
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Genries'
        context['url_update_name'] = 'referencies:genrie-update'
        context['url_delete_name'] = 'referencies:genrie-delete'
        return context

class DetailGenrie(LoginRequiredMixin, generic.DetailView):
    model = models.Genrie
    login_url = reverse_lazy('login')
    template_name = 'referencies/detail.html'

class CreateGenrie(LoginRequiredMixin, generic.CreateView):
    model = models.Genrie
    login_url = reverse_lazy('login')
    form_class = forms.GenrieGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:genrie-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateGenrie(LoginRequiredMixin, generic.UpdateView):
    model = models.Genrie
    login_url = reverse_lazy('login')
    form_class = forms.GenrieGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:genrie-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteGenrie(LoginRequiredMixin, generic.DeleteView):
    model = models.Genrie
    login_url = reverse_lazy('login')
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:genrie-list')



class ListPublishingHouse(LoginRequiredMixin, generic.ListView):
    model = models.PublishingHouse
    login_url = reverse_lazy('login')
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Publishing Houses'
        context['url_update_name'] = 'referencies:ph-update'
        context['url_delete_name'] = 'referencies:ph-delete'
        return context

class DetailPublishingHouse(LoginRequiredMixin, generic.DetailView):
    model = models.PublishingHouse
    login_url = reverse_lazy('login')
    template_name = 'referencies/detail.html'

class CreatePublishingHouse(LoginRequiredMixin, generic.CreateView):
    model = models.PublishingHouse
    login_url = reverse_lazy('login')
    form_class = forms.PublishingHouseGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:ph-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdatePublishingHouse(LoginRequiredMixin, generic.UpdateView):
    model = models.PublishingHouse
    login_url = reverse_lazy('login')
    form_class = forms.PublishingHouseGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:ph-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeletePublishingHouse(LoginRequiredMixin, generic.DeleteView):
    model = models.PublishingHouse
    login_url = reverse_lazy('login')
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:ph-list')



class ListUnits(LoginRequiredMixin, generic.ListView):
    model = models.Units
    login_url = reverse_lazy('login')
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Units'
        context['url_update_name'] = 'referencies:units-update'
        context['url_delete_name'] = 'referencies:units-delete'
        return context

class DetailUnits(LoginRequiredMixin, generic.DetailView):
    model = models.Units
    login_url = reverse_lazy('login')
    template_name = 'referencies/detail.html'

class CreateUnits(LoginRequiredMixin, generic.CreateView):
    model = models.Units
    login_url = reverse_lazy('login')
    form_class = forms.UnitsGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:units-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateUnits(LoginRequiredMixin, generic.UpdateView):
    model = models.Units
    login_url = reverse_lazy('login')
    form_class = forms.UnitsGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:units-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteUnits(LoginRequiredMixin, generic.DeleteView):
    model = models.Units
    login_url = reverse_lazy('login')
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:units-list')


class ListCover(LoginRequiredMixin, generic.ListView):
    model = models.Cover
    login_url = reverse_lazy('login')
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Covers'
        context['url_update_name'] = 'referencies:cover-update'
        context['url_delete_name'] = 'referencies:cover-delete'
        return context

class DetailCover(LoginRequiredMixin, generic.DetailView):
    model = models.Cover
    login_url = reverse_lazy('login')
    template_name = 'referencies/detail.html'

class CreateCover(LoginRequiredMixin, generic.CreateView):
    model = models.Cover
    login_url = reverse_lazy('login')
    form_class = forms.CoverGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:cover-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateCover(LoginRequiredMixin, generic.UpdateView):
    model = models.Cover
    login_url = reverse_lazy('login')
    form_class = forms.CoverGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:cover-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteCover(LoginRequiredMixin, generic.DeleteView):
    model = models.Cover
    login_url = reverse_lazy('login')
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:cover-list')


class ListAgeLimit(LoginRequiredMixin, generic.ListView):
    model = models.AgeLimit
    login_url = reverse_lazy('login')
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Age Limits'
        context['url_update_name'] = 'referencies:al-update'
        context['url_delete_name'] = 'referencies:al-delete'
        return context

class DetailAgeLimit(LoginRequiredMixin, generic.DetailView):
    model = models.AgeLimit
    login_url = reverse_lazy('login')
    template_name = 'referencies/detail.html'

class CreateAgeLimit(LoginRequiredMixin, generic.CreateView):
    model = models.AgeLimit
    login_url = reverse_lazy('login')
    form_class = forms.AgeLimitGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:al-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateAgeLimit(LoginRequiredMixin, generic.UpdateView):
    model = models.AgeLimit
    login_url = reverse_lazy('login')
    form_class = forms.AgeLimitGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:al-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteAgeLimit(LoginRequiredMixin, generic.DeleteView):
    model = models.AgeLimit
    login_url = reverse_lazy('login')
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:al-list')



class ListRate(LoginRequiredMixin, generic.ListView):
    model = models.Rate
    login_url = reverse_lazy('login')
    template_name = 'referencies/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'List of Rates'
        context['url_update_name'] = 'referencies:rate-update'
        context['url_delete_name'] = 'referencies:rate-delete'
        return context

class DetailRate(LoginRequiredMixin, generic.DetailView):
    model = models.Rate
    login_url = reverse_lazy('login')
    template_name = 'referencies/detail.html'

class CreateRate(LoginRequiredMixin, generic.CreateView):
    model = models.Rate
    login_url = reverse_lazy('login')
    form_class = forms.RateGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:rate-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateRate(LoginRequiredMixin, generic.UpdateView):
    model = models.Rate
    login_url = reverse_lazy('login')
    form_class = forms.RateGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:rate-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteRate(LoginRequiredMixin, generic.DeleteView):
    model = models.Rate
    login_url = reverse_lazy('login')
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:rate-list')