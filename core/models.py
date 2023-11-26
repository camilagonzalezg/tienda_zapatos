from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.
class Profesion(models.Model):
    profesion = models.CharField(max_length=200, help_text="Ingresa tu profesion")
    
    #Subclase para que en el admin no se vea "profesions", sino "profesiones"
    class Meta:
        verbose_name="Profesion"
        verbose_name_plural="Profesiones"
    
    def __str__(self):
        return f'{self.profesion}'

    #Devuelve la url de una instancia particular del modelo Producto
    def get_absolute_url(self):
        return reverse('profesion-detail', kwargs={"pk": self.id})

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, help_text="Ingresa tu nombre")
    apellido = models.CharField(max_length=100, help_text="Ingresa tu apellido")
    fecha_nac = models.DateField(null=True, max_length=100, help_text="Ingresa tu fecha de nacimiento")
    correo = models.EmailField(null=True, blank=True, help_text="Ingresa tu email")
    #Se coloca Profesion sin '', porque la clase se creó arriba
    profesion = models.ManyToManyField(Profesion, help_text="Ingresa la profesion")

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.fecha_nac} {self.correo}'

    #Devuelve la url de una instancia particular del modelo Producto
    def get_absolute_url(self):
        return reverse('cliente-detail', kwargs={"pk": self.id})
    
    # Para agregar el campo profesional display del aadmin en django
    def display_profesion(self):
    # Se crea un string con las profesiones
        return ', '.join([prof.profesion for prof in self.profesion.all()[:3]])

    #Con el metodo anterior hecho, se despliega la profesion
    display_profesion.short_description = 'Profesion'
    
class Contacto(models.Model):
    email = models.EmailField(max_length=100, help_text="Ingresa tu email")
    asunto = models.CharField(max_length=100, help_text="Ingresa tu ausnto")
    mensaje = models.CharField(max_length=100, help_text="Ingresa tu mensaje")
    copia = models.BooleanField(default=False, help_text="¿Con copia?")

    def __str__(self):
        return f'{self.email}'

    #Devuelve la url de una instancia particular del modelo Producto
    def get_absolute_url(self):
        return reverse('contacto-detail', kwargs={"pk": self.id})

class Producto(models.Model):
    nombre = models.CharField(max_length=100, help_text="Ingresa tu nombre")
    stock = models.IntegerField(help_text="Stock de producto")
    precio = models.IntegerField(null=True, help_text="Precio de producto")
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    SKU = models.CharField(max_length=100, help_text="Ingresa el SKU del producto", default="")
    descripcion = models.TextField(help_text="Descripción del producto", default="")
    calificacion = models.IntegerField(null=True, help_text="Calificación del producto de 1 a 5", validators=[MinValueValidator(1), MaxValueValidator(5)])
    oferta = models.BooleanField(default=False, help_text="¿El producto está en oferta?")
    precioanterior = models.IntegerField(null=True, help_text="Precio anterior del producto en oferta")
    precioactual = models.IntegerField(null=True, help_text="Precio actual del producto")
    imagen1 = models.ImageField(null=True, upload_to='productos', help_text="Imagen en lista del producto")
    imagen2 = models.ImageField(null=True, upload_to='productos', help_text="Imagen detalle del producto")
    
    def __str__(self):
        return f'{self.nombre} {self.stock} {self.precio} {self.categoria} {self.SKU} {self.descripcion} {self.calificacion} {self.oferta} {self.precioanterior} {self.precioactual} {self.imagen1} {self.imagen2}'

    #Devuelve la url de una instancia particular del modelo Producto
    def get_absolute_url(self):
        return reverse('producto-detail', kwargs={"pk": self.id})

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, help_text="Ingresa nombre de categoría")
    def __str__(self):
        return f'{self.nombre}'

    #Devuelve la url de una instancia particular del modelo Producto
    def get_absolute_url(self):
        return reverse('categoria-detail', kwargs={"pk": self.id})