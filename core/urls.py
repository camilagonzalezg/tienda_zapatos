from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('producto/', views.producto, name='producto'),
    path('formulario/', views.formulario, name='formulario'),
]
