from django.urls import path
from . import views
app_name='orders'

urlpatterns=[
    path('cart/', views.show_cart, name='show-cart'),
    path('del-position/<int:pk>/', views.DelPosition.as_view(), name='del-position'),
    path('upd-position/<int:pk>/', views.UpdatePosition.as_view(), name='upd-position'),
    path('create-order/', views.Order.as_view(), name='create-order'),
    path('success/', views.OrderSuccess.as_view(), name='order-success'),
    path('order/<int:pk>/', views.OrderDetail.as_view(), name='detail-order'),
    path('order/', views.OrderList.as_view(), name='list-order'),
    path('order/all/', views.OrderAllList.as_view(), name='list-allorder'),
    path('del-order/<int:pk>/', views.DelOrder.as_view(), name='delete-order'),
    path('upd-order/<int:pk>/', views.UpdateOrder.as_view(), name='update-order'),
    path('upd-bic/<int:pk>/', views.UpdateBookInCart.as_view(), name='update-bic'),
    path('cr-com/', views.CreateOrderComment.as_view(), name='create-order-comment'),
    path('cr-com/success', views.CreateOrderComment.as_view(), name='create-order-comment'),
 
    ]