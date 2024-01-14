from django.urls import path
from .views import index, random_view

urlpatterns = [
    path('', index, name='index'),
    path('r/', random_view, name='random'),
]
