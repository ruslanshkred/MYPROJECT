from . import models, forms
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

class ListAuthor(generic.ListView):
    model = models.Author
    template_name = 'referencies/list_author.html'

class DetailAuthor(generic.DetailView):
    model = models.Author   
    template_name = 'referencies/detail.html'

class CreateAuthor(generic.CreateView):
    model = models.Author
    form_class = forms.AuthorGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:author-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Создать'
        return context

class UpdateAuthor(generic.UpdateView):
    model = models.Author
    form_class = forms.AuthorGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:author-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Обновить'
        return context
    
class DeleteAuthor(generic.DeleteView):
    model = models.Author
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:author-list')


class ListSerie(generic.ListView):
    model = models.Serie
    template_name = 'referencies/list_serie.html'

class DetailSerie(generic.DetailView):
    model = models.Serie
    template_name = 'referencies/detail.html'

class CreateSerie(generic.CreateView):
    model = models.Serie
    form_class = forms.SerieGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:serie-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Создать'
        return context

class UpdateSerie(generic.UpdateView):
    model = models.Serie
    form_class = forms.SerieGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:serie-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Обновить'
        return context

class DeleteSerie(generic.DeleteView):
    model = models.Serie
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:serie-list')


class ListGenrie(generic.ListView):
    model = models.Genrie
    template_name = 'referencies/list_genrie.html'

class DetailGenrie(generic.DetailView):
    model = models.Genrie
    template_name = 'referencies/detail.html'

class CreateGenrie(generic.CreateView):
    model = models.Genrie
    form_class = forms.GenrieGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:genrie-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Создать'
        return context

class UpdateGenrie(generic.UpdateView):
    model = models.Genrie
    form_class = forms.GenrieGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:genrie-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Обновить'
        return context

class DeleteGenrie(generic.DeleteView):
    model = models.Genrie
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:genrie-list')



class ListPublishingHouse(generic.ListView):
    model = models.PublishingHouse
    template_name = 'referencies/list_ph.html'

class DetailPublishingHouse(generic.DetailView):
    model = models.PublishingHouse
    template_name = 'referencies/detail.html'

class CreatePublishingHouse(generic.CreateView):
    model = models.PublishingHouse
    form_class = forms.PublishingHouseGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:ph-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Создать'
        return context

class UpdatePublishingHouse(generic.UpdateView):
    model = models.PublishingHouse
    form_class = forms.PublishingHouseGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:ph-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Обновить'
        return context

class DeletePublishingHouse(generic.DeleteView):
    model = models.PublishingHouse
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:ph-list')



class ListUnits(generic.ListView):
    model = models.Units
    template_name = 'referencies/list_units.html'

class DetailUnits(generic.DetailView):
    model = models.Units
    template_name = 'referencies/detail.html'

class CreateUnits(generic.CreateView):
    model = models.Units
    form_class = forms.UnitsGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:units-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Создать'
        return context

class UpdateUnits(generic.UpdateView):
    model = models.Units
    form_class = forms.UnitsGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:units-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Обновить'
        return context

class DeleteUnits(generic.DeleteView):
    model = models.Units
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:units-list')


class ListCover(generic.ListView):
    model = models.Cover
    template_name = 'referencies/list_cover.html'

class DetailCover(generic.DetailView):
    model = models.Cover
    template_name = 'referencies/detail.html'

class CreateCover(generic.CreateView):
    model = models.Cover
    form_class = forms.CoverGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:cover-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Создать'
        return context

class UpdateCover(generic.UpdateView):
    model = models.Cover
    form_class = forms.CoverGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:cover-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Обновить'
        return context

class DeleteCover(generic.DeleteView):
    model = models.Cover
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:cover-list')


class ListAgeLimit(generic.ListView):
    model = models.AgeLimit
    template_name = 'referencies/list-al.html'

class DetailAgeLimit(generic.DetailView):
    model = models.AgeLimit
    template_name = 'referencies/detail.html'

class CreateAgeLimit(generic.CreateView):
    model = models.AgeLimit
    form_class = forms.AgeLimitGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:al-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Создать'
        return context

class UpdateAgeLimit(generic.UpdateView):
    model = models.AgeLimit
    form_class = forms.AgeLimitGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:al-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Обновить'
        return context

class DeleteAgeLimit(generic.DeleteView):
    model = models.AgeLimit
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:al-list')



class ListRate(generic.ListView):
    model = models.Rate
    template_name = 'referencies/list-rate.html'

class DetailRate(generic.DetailView):
    model = models.Rate
    template_name = 'referencies/detail.html'

class CreateRate(generic.CreateView):
    model = models.Rate
    form_class = forms.RateGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:rate-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Создать'
        return context

class UpdateRate(generic.UpdateView):
    model = models.Rate
    form_class = forms.RateGroup
    template_name = 'referencies/edit.html'
    success_url = reverse_lazy('referencies:rate-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Обновить'
        return context

class DeleteRate(generic.DeleteView):
    model = models.Rate
    template_name = 'referencies/delete.html'
    success_url = reverse_lazy('referencies:rate-list')