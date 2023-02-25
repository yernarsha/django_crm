from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customer/<int:pk>', views.get_customer, name='customer'),
    path('delete_customer/<int:pk>', views.delete_customer, name='delete_customer'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('update_customer/<int:pk>', views.update_customer, name='update_customer'),
]