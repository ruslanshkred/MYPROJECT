from django.urls import path
from . import views

app_name='homepage'

urlpatterns=[
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('profile-create/', views.Profile.as_view(), name='profile-create'),
    path('profile-list/', views.ListProfile.as_view(), name='profile-list'),
    path('profile/<int:pk>/', views.DetailProfile.as_view(), name='profile-detail'),
    path('profile-update/<int:pk>/', views.UpdateProfile.as_view(), name='profile-update'),
    path('profile-delete/<int:pk>/', views.DeleteProfile.as_view(), name='profile-delete'),
    path('delivery/', views.Delivery.as_view(), name='delivery'),
    path('search/', views.SearchResultsView.as_view(), name='search-results'),
    
    ]