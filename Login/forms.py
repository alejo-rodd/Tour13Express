from django.db import models  
from django.forms import fields  
from .models import Producto 
from django import forms  
  
  
class ProductoForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = Producto
        fields = ['nombre_prod', 'descripcion_prod', 'imagen_prod','activo', 'precio']
        widgets = {
            'nombre_prod': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre del producto'}),
            'descripcion_prod': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Escribe la descripción', 'rows':'3'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'precio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el precio'}),
            'imagen_prod': forms.FileInput(attrs={'class': 'form-control'}),
        }

        help_texts = {
            'activo': '<p class="text-warning">Marcar la casilla si hay productos disponibles</p>',
        }

        labels = {
            'nombre_prod': 'Nombre del producto:',
            'descripcion_prod': 'Descripción personalizada:',
            'activo': 'Disponible:',
            'precio': 'Precio:',
            'imagen_prod': 'Imagen del producto:',
        }