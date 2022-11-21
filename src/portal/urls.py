from django.urls import path
from . import views
app_name='portal'

urlpatterns=[
    path('', views.Portal.as_view(), name = 'portal')
    
    # path(views.ListAuthor.as_view(), name='author-list'),
    # path('author/<int:pk>/', views.DetailAuthor.as_view(), name='author-detail'),
    # path('author-create/', views.CreateAuthor.as_view(), name='author-create'),
    # path('author-update/<int:pk>/', views.UpdateAuthor.as_view(), name='author-update'),
    # path('author-delete/<int:pk>/', views.DeleteAuthor.as_view(), name='author-delete'),

]