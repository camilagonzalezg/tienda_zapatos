from rest_framework import serializers
from .models import Ordenes

# Seriealizadores que definen la representación de la API.
class OrdenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordenes
        fields = ['id', 'fecha_emision', 'cliente', 'producto', 'cantidad', 'precio', 'total']
        read_only_fields = ('fecha_emision',)    