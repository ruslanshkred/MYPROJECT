from django.urls import path
from . import views
app_name='books'

urlpatterns=[
    path('book/', views.ListBook.as_view(), name='book-list'),
    path('book-show/', views.ShowBooks.as_view(), name='book-show'),
    path('book/<int:pk>/', views.DetailBook.as_view(), name='book-detail'),
    path('book-create/', views.CreateBook.as_view(), name='book-create'),
    path('book-update/<int:pk>/', views.UpdateBook.as_view(), name='book-update'),
    path('book-delete/<int:pk>/', views.DeleteBook.as_view(), name='book-delete'),

    path('book-detective/', views.ShowDetective.as_view(), name='book-detective'),
    path('book-fantastic/', views.ShowFantastic.as_view(), name='book-fantastic'),
    path('book-novel/', views.ShowNovel.as_view(), name='book-novel'),

    path('comment/', views.ListBookComment.as_view(), name='book-comment-list'),
    path('comment-create/', views.CreateBookComment.as_view(), name='comment-create'),
    ]