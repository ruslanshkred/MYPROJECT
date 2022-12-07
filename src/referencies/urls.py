from django.urls import path
from . import views
app_name='referencies'

urlpatterns=[
    path('author/', views.ListAuthor.as_view(), name='author-list'),
    path('author/<int:pk>/', views.DetailAuthor.as_view(), name='author-detail'),
    path('author-create/', views.CreateAuthor.as_view(), name='author-create'),
    path('author-update/<int:pk>/', views.UpdateAuthor.as_view(), name='author-update'),
    path('author-delete/<int:pk>/', views.DeleteAuthor.as_view(), name='author-delete'),

    path('serie/', views.ListSerie.as_view(), name='serie-list'),
    path('serie/<int:pk>/', views.DetailSerie.as_view(), name='serie-detail'),
    path('serie-create/', views.CreateSerie.as_view(), name='serie-create'),
    path('serie-update/<int:pk>/', views.UpdateSerie.as_view(), name='serie-update'),
    path('serie-delete/<int:pk>/', views.DeleteSerie.as_view(), name='serie-delete'),

    path('genrie/', views.ListGenrie.as_view(), name='genrie-list'),
    path('genrie/<int:pk>/', views.DetailGenrie.as_view(), name='genrie-detail'),
    path('genrie-create/', views.CreateGenrie.as_view(), name='genrie-create'),
    path('genrie-update/<int:pk>/', views.UpdateGenrie.as_view(), name='genrie-update'),
    path('genrie-delete/<int:pk>/', views.DeleteGenrie.as_view(), name='genrie-delete'),

    path('ph/', views.ListPublishingHouse.as_view(), name='ph-list'),
    path('ph/<int:pk>/', views.DetailPublishingHouse.as_view(), name='ph-detail'),
    path('ph-create/', views.CreatePublishingHouse.as_view(), name='ph-create'),
    path('ph-update/<int:pk>/', views.UpdatePublishingHouse.as_view(), name='ph-update'),
    path('ph-delete/<int:pk>/', views.DeletePublishingHouse.as_view(), name='ph-delete'),

    path('units/', views.ListUnits.as_view(), name='units-list'),
    path('units/<int:pk>/', views.DetailUnits.as_view(), name='units-detail'),
    path('units-create/', views.CreateUnits.as_view(), name='units-create'),
    path('units-update/<int:pk>/', views.UpdateUnits.as_view(), name='units-update'),
    path('units-delete/<int:pk>/', views.DeleteUnits.as_view(), name='units-delete'),

    path('cover/', views.ListCover.as_view(), name='cover-list'),
    path('cover/<int:pk>/', views.DetailCover.as_view(), name='cover-detail'),
    path('cover-create/', views.CreateCover.as_view(), name='cover-create'),
    path('cover-update/<int:pk>/', views.UpdateCover.as_view(), name='cover-update'),
    path('cover-delete/<int:pk>/', views.DeleteCover.as_view(), name='cover-delete'),

    path('al/', views.ListAgeLimit.as_view(), name='al-list'),
    path('al/<int:pk>/', views.DetailAgeLimit.as_view(), name='al-detail'),
    path('al-create/', views.CreateAgeLimit.as_view(), name='al-create'),
    path('al-update/<int:pk>/', views.UpdateAgeLimit.as_view(), name='al-update'),
    path('al-delete/<int:pk>/', views.DeleteAgeLimit.as_view(), name='al-delete'),

    path('rate/', views.ListRate.as_view(), name='rate-list'),
    path('rate/<int:pk>/', views.DetailRate.as_view(), name='rate-detail'),
    path('rate-create/', views.CreateRate.as_view(), name='rate-create'),
    path('rate-update/<int:pk>/', views.UpdateRate.as_view(), name='rate-update'),
    path('rate-delete/<int:pk>/', views.DeleteRate.as_view(), name='rate-delete'),

    path('status/', views.ListStatus.as_view(), name='status-list'),
    path('status/<int:pk>/', views.DetailStatus.as_view(), name='status-detail'),
    path('status-create/', views.CreateStatus.as_view(), name='status-create'),
    path('status-update/<int:pk>/', views.UpdateStatus.as_view(), name='status-update'),
    path('status-delete/<int:pk>/', views.DeleteStatus.as_view(), name='status-delete'),
] 