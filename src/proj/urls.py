"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from referencies import views as st_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', st_views.ListAuthor.as_view()),
    path('author/<int:pk>/', st_views.DetailAuthor.as_view()),
    path('author-create/', st_views.CreateAuthor.as_view()),
    path('author-update/<int:pk>/', st_views.UpdateAuthor.as_view()),
    path('author-delete/<int:pk>/', st_views.DeleteAuthor.as_view()),

    path('serie/', st_views.ListSerie.as_view()),
    path('serie/<int:pk>/', st_views.DetailSerie.as_view()),
    path('serie-create/', st_views.CreateSerie.as_view()),
    path('serie-update/<int:pk>/', st_views.UpdateSerie.as_view()),
    path('serie-delete/<int:pk>/', st_views.DeleteSerie.as_view()),

    path('genrie/', st_views.ListGenrie.as_view()),
    path('genrie/<int:pk>/', st_views.DetailGenrie.as_view()),
    path('genrie-create/', st_views.CreateGenrie.as_view()),
    path('genrie-update/<int:pk>/', st_views.UpdateGenrie.as_view()),
    path('genrie-delete/<int:pk>/', st_views.DeleteGenrie.as_view()),

    path('author/', st_views.ListAuthor.as_view()),
    path('author/<int:pk>/', st_views.DetailAuthor.as_view()),
    path('author-create/', st_views.CreateAuthor.as_view()),
    path('author-update/<int:pk>/', st_views.UpdateAuthor.as_view()),
    path('author-delete/<int:pk>/', st_views.DeleteAuthor.as_view()),

    path('ph/', st_views.ListPublishingHouse.as_view()),
    path('ph/<int:pk>/', st_views.DetailPublishingHouse.as_view()),
    path('ph-create/', st_views.CreatePublishingHouse.as_view()),
    path('ph-update/<int:pk>/', st_views.UpdatePublishingHouse.as_view()),
    path('ph-delete/<int:pk>/', st_views.DeletePublishingHouse.as_view()),

    path('units/', st_views.ListUnits.as_view()),
    path('units/<int:pk>/', st_views.DetailUnits.as_view()),
    path('units-create/', st_views.CreateUnits.as_view()),
    path('units-update/<int:pk>/', st_views.UpdateUnits.as_view()),
    path('units-delete/<int:pk>/', st_views.DeleteUnits.as_view()),

]
