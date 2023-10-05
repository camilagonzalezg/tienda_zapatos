from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "core/index.html")

def productos(request):
    return render(request, "core/productos.html")

def producto(request):
    
    #Datos parta renderizar  
    #Se genera diccionario con información de los zapatos.
    productos =  {"zapato1": {"nombre":"Zapatillas", 
                "precio":"$35.000", 
                "imagen": "zapatillas.jpg" },
                "zapato2": {"nombre":"Botas", 
                "precio":"$60.000", 
                "imagen": "botas.jpg" },
                "zapato3": {"nombre":"Chalas", 
                "precio":"$25.000", 
                "imagen": "chalas.jpg" },
                "zapato4": {"nombre":"Pantuflas", 
                "precio":"$20.000", 
                "imagen": "pantuflas.jpg" },
                "zapato5": {"nombre":"Mocasines", 
                "precio":"$30.000", 
                "imagen": "mocasines.jpg" },
                "zapato6": {"nombre":"Crocs", 
                "precio":"$25.000", 
                "imagen": "crocs.jpg" },
                "zapato7": {"nombre":"Bamers", 
                "precio":"$35.000", 
                "imagen": "bamers.jpg" },
                "zapato8": {"nombre":"Condoritas", 
                "precio":"$15.000", 
                "imagen": "condoritas.jpg" },
                }
    
    return render(request, "core/producto.html", productos)

def formulario(request):
    return render(request, "core/formulario.html")