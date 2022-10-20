from . import models, forms
from django.views import generic

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
    template_name = 'referencies/create.html'

class UpdateAuthor(generic.UpdateView):
    model = models.Author
    form_class = forms.AuthorGroup
    template_name = 'referencies/update.html'

class DeleteAuthor(generic.DeleteView):
    model = models.Author
    template_name = 'referencies/delete.html'



class ListSerie(generic.ListView):
    model = models.Serie
    template_name = 'referencies/list_serie.html'

class DetailSerie(generic.DetailView):
    model = models.Serie
    template_name = 'referencies/detail.html'

class CreateSerie(generic.CreateView):
    model = models.Serie
    form_class = forms.SerieGroup
    template_name = 'referencies/create.html'

class UpdateSerie(generic.UpdateView):
    model = models.Serie
    form_class = forms.SerieGroup
    template_name = 'referencies/update.html'

class DeleteSerie(generic.DeleteView):
    model = models.Serie
    template_name = 'referencies/delete.html'


class ListGenrie(generic.ListView):
    model = models.Genrie
    template_name = 'referencies/list_genrie.html'

class DetailGenrie(generic.DetailView):
    model = models.Genrie
    template_name = 'referencies/detail.html'

class CreateGenrie(generic.CreateView):
    model = models.Genrie
    form_class = forms.GenrieGroup
    template_name = 'referencies/create.html'

class UpdateGenrie(generic.UpdateView):
    model = models.Genrie
    form_class = forms.GenrieGroup
    template_name = 'referencies/update.html'

class DeleteGenrie(generic.DeleteView):
    model = models.Genrie
    template_name = 'referencies/delete.html'


class ListPublishingHouse(generic.ListView):
    model = models.PublishingHouse
    template_name = 'referencies/list_ph.html'

class DetailPublishingHouse(generic.DetailView):
    model = models.PublishingHouse
    template_name = 'referencies/detail.html'

class CreatePublishingHouse(generic.CreateView):
    model = models.PublishingHouse
    form_class = forms.PublishingHouseGroup
    template_name = 'referencies/create.html'

class UpdatePublishingHouse(generic.UpdateView):
    model = models.PublishingHouse
    form_class = forms.PublishingHouseGroup
    template_name = 'referencies/update.html'

class DeletePublishingHouse(generic.DeleteView):
    model = models.PublishingHouse
    template_name = 'referencies/delete.html'


class ListUnits(generic.ListView):
    model = models.Units
    template_name = 'referencies/list_units.html'

class DetailUnits(generic.DetailView):
    model = models.Units
    template_name = 'referencies/detail.html'

class CreateUnits(generic.CreateView):
    model = models.Units
    form_class = forms.UnitsGroup
    template_name = 'referencies/create.html'

class UpdateUnits(generic.UpdateView):
    model = models.Units
    form_class = forms.UnitsGroup
    template_name = 'referencies/update.html'

class DeleteUnits(generic.DeleteView):
    model = models.Units
    template_name = 'referencies/delete.html'