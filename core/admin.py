from django.contrib import admin
from.models import Cliente, Producto, Categoria, Contacto, Profesion

# Register your models here.

#3) Se utiliza clase en la definicion de modelos relacionados/para ver categorias
#class ProductoInline(admin.TabularInline):
class ProductoInline(admin.StackedInline):
	model = Producto
 #Permite definir los registros adicionales
    #extra = 1

# 2) Se regsitran las clases que queremos visualizar en el admin de django
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'fecha_nac', 'correo', 'display_profesion')
    list_filter = ('apellido', 'fecha_nac')
    fieldsets = (
	    ('Información Personal', {
            'fields': ('nombre', 'apellido')
        }),
     	('Información Adicional', {
            'fields': ('fecha_nac', 'correo', 'profesion')
        })
        )
    
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'asunto', 'mensaje', 'copia', 'nombre', 'apellido')
    list_filter = ('email', )
    
class ProfesionAdmin(admin.ModelAdmin):
    list_display = ('id', 'profesion')
    list_filter = ('profesion',)
     
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'stock', 'precio', 'categoria', 'SKU','descripcion',
                    'calificacion','oferta','precioanterior','precioactual')
    list_filter = ('nombre', 'stock')
    
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_filter = ('nombre',)
    inlines = [ProductoInline]

# 1) Se registran las clases
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Profesion, ProfesionAdmin)