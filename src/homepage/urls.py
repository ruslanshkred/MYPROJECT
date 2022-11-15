from django.urls import path
from . import views

app_name='homepage'

urlpatterns=[
    path("signup/", views.SignUp.as_view(), name="signup"),
    
       
]