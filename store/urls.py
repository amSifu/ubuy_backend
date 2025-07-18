from django.urls import path 
from .views import store, create_product

urlpatterns = [
    path('', store),
    path('create/', create_product)
]
