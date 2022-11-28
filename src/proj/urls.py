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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from homepage.views import HomePage
from homepage import views
from portal import views


urlpatterns = [
    path('s-admin/', admin.site.urls),
    #path('login/', auth_views.LoginView.as_view(template_name='homepage/login.html'), name='login'),
    #path('register/', views.UserCreationForm, name = 'register'),
    path('ref/', include('referencies.urls', namespace='referencies')),
    path('book/', include('books.urls', namespace='books')),
    path('', HomePage.as_view(), name = 'home_page'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
 #   path("signup/", views.SignUp.as_view(), name="signup"),
    path('home/', include('homepage.urls', namespace='homepage')),
 #   path('profile/', views.Profile.as_view(), name='profile')
    path('portal/', include('portal.urls', namespace='portal')),
    path('orders/', include('orders.urls', namespace='orders'))


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)