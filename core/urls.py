from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #Index
    path('index/', views.index, name='index'),
    #Formulario de contacto
    path('formulario/', views.formcontacto, name="formcontacto"),
    path('gracias/', views.gracias),
    # Busquedas
    path('buscar/', views.buscar_productos, name='buscar'),
    path('prodsxcateg/', views.productos_categoria, name='productos-categoria'),
    #Listas
    path('productos/', views.ProductoListView.as_view(), name='productos'),
    path('contactos/', views.ContactoListView.as_view(), name='contactos'),
    path('clientes/', views.ClienteListView.as_view(), name='clientes'),
    path('categorias/', views.CategoriaListView.as_view(), name='categorias'),
    path('formulario/', views.formulario, name='formulario'),
    #Detalles
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto-detail'),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente-detail'),
    path('contacto/<int:pk>/', views.ContactoDetailView.as_view(), name='contacto-detail'),
    path('categoria/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria-detail'),
    # Vistas de edición genérica
    path('producto/add/', views.ProductoCreateView.as_view(), name='producto-add'),
    path('producto/<int:pk>/update/', views.ProductoUpdateView.as_view(), name='producto-update'),
    path('producto/<int:pk>/delete/', views.ProductoDeleteView.as_view(), name='producto-delete'),
]
