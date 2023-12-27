from django.shortcuts import render
from .models import Cliente, Producto, Categoria, Contacto, Ordenes
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import FormularioContacto
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from .serializers import OrdenesSerializer
from .services import get_users, get_ordenes

# Create your views here.
def index(request):
    #Generacion de contadores para los modelos
    cant_clientes = Cliente.objects.all().count()
    cant_productos = Producto.objects.all().count()
    cant_categorias = Categoria.objects.all().count()
    #Obtencion de productos en la categoria "varios"
    prod_categoria = Producto.objects.filter(categoria__exact = '4').count()
    # Manejo de sesiones
    # Obtener la cantidad de visitas desde la sesión e incrementarla
    num_visitas = request.session.get("num_visitas",1)
    request.session["num_visitas"] = num_visitas + 1
    contexto = {'cant_clientes': cant_clientes,
                'cant_productos': cant_productos,
                'cant_categoria': cant_categorias,
                'prod_categoria': prod_categoria,
                'visitas': num_visitas,
                }
    return render(request, 'core/index.html', contexto)

class ProductoListView(generic.ListView):
    model = Producto
    # Paginacion
    paginate_by = 7
    
class CategoriaListView(generic.ListView):
    model = Categoria
    
class ClienteListView(generic.ListView):
    model = Cliente

class ContactoListView(generic.ListView):
    model = Contacto
    # Paginacion
    paginate_by = 5
    
#Vistas para busquedas
def buscar_productos(request):
    categorias = Categoria.objects.all()
    return render(request, "core/buscar_productos.html", {'categorias':categorias})

def productos_categoria(request):
    # Se utiliza el objeto request para obtener el parametro de la peticion
    if request.GET['cod_categoria'] and request.GET['cod_categoria'] !='0':
        cod_categoria = request.GET['cod_categoria']
        # Se recuperan del modelo Producto, los productos de la categoria
        lst_productos = Producto.objects.filter(categoria__exact=cod_categoria)
        # Se busca el objeto de la Categoria
        categoria = Categoria.objects.get(id__exact=cod_categoria)
        # Se genera un contexto
        contexto = {'productos':lst_productos,'categoria':categoria}
    else:
        contexto = {'categoria':'Debes seleccionar una categoria'}
    return render(request, "core/productos_categoria.html", contexto)

# Formulario de contacto
# Vista que atiende las peticiones
def formcontacto(request):
    if request.method == 'POST':
        # Se crea una instancia del formulario (Clase de forms.py)
        form = FormularioContacto(request.POST)
        # Se verifica si el formulario es valido
        if form.is_valid():
            # Se obtiene informacion del formulario
            # Se utiliza la lista "cleaned_data"
            nombreform = form.cleaned_data['nombre']
            apellidoform = form.cleaned_data['apellido']
            asuntoform = form.cleaned_data['asunto']
            emailform = form.cleaned_data['email']
            mensajeform = form.cleaned_data['mensaje']
            cc_ami = form.cleaned_data['cc_ami']
            recipients = ['camilag@gmail.com']
            
            # Se puede enviar un correo
            # Se agrega lista de destinatarios
            if cc_ami:
                recipients.append(emailform)
                
            #Se puede enviar un correo
            send_mail(asuntoform, mensajeform, emailform, recipients)

            # Se puede guardar en la bbdd en un Modelo de contacto
            contacto = Contacto(nombre=nombreform, apellido=apellidoform, asunto=asuntoform, email=emailform, mensaje=mensajeform, copia=cc_ami)
            contacto.save()
            return HttpResponseRedirect('/core/gracias')
    else:
        form = FormularioContacto()
    return render(request, 'core/formulario.html', {'form':form})
    
def gracias(request):
    return render(request, 'core/gracias.html')

#Creacion de vistas en detalle, basada en clases
class ProductoDetailView(generic.DetailView):
    model = Producto

class ClienteDetailView(generic.DetailView):
    model = Cliente
    
class CategoriaDetailView(generic.DetailView):
    model = Categoria
    
class ContactoDetailView(generic.DetailView):
    model = Contacto

# MANTENEDORES DE PRODUCTOS
# Vistas de edicion generica
class ProductoCreateView(CreateView):
    model = Producto
    fields = ['id', 'nombre', 'precioactual', 'stock', 'imagen1', 'imagen2', 'categoria']
    initial = {'stock':'0'}

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['id', 'nombre', 'precioactual', 'stock', 'imagen1', 'imagen2', 'categoria']
    template_name_suffix = "_update_form"

class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy("productos")
    
def formulario(request):
    return render(request, "core/formulario.html")

def producto(request):
    return render(request, "core/producto.html")

def contacto(request):
    return render(request, "core/contacto.html")

class OrdenesViewSet(viewsets.ModelViewSet):
    # Origen de data.
    queryset = Ordenes.objects.all()
    # Permisos para las apps clientes
    permission_classes = [permissions.AllowAny]
    # Se indica el serializador
    serializer_class = OrdenesSerializer
    
# Vista para consumir la API
def muestra_usuarios_api(request):
    params = {'page':'1'}
    context = {
        'users': get_users(params)
    } 
    return render(request, 'core/usuarios.html', context)

def muestra_ordenes(request):
    params = {}
    context = {
        'ordenes': get_ordenes(params)
    } 
    return render(request, 'core/ordenes.html', context)