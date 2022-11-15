from django.urls import path
from . import views
app_name='books'

urlpatterns=[
    path('book/', views.ListBook.as_view(), name='book-list'),
    path('book/<int:pk>/', views.DetailBook.as_view(), name='book-detail'),
    path('book-create/', views.CreateBook.as_view(), name='book-create'),
    path('book-update/<int:pk>/', views.UpdateBook.as_view(), name='book-update'),
    path('book-delete/<int:pk>/', views.DeleteBook.as_view(), name='book-delete'),
    ]