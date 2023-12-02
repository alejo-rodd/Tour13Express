from django.db import models
from django.contrib.auth.models import User

#para eliminar imagen
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

# Create your models here.
class Producto(models.Model):
    nombre_prod = models.CharField(max_length=50)
    descripcion_prod = models.CharField(max_length=150)  
    imagen_prod = models.ImageField(upload_to='images', null = True)
    activo = models.BooleanField(default=True)
    precio = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
  
    def __str__(self):  
        return self.nombre_prod + ' - ' + self.precio


@receiver(pre_delete, sender=Producto)
def eliminar_archivo_imagen(sender, instance, **kwargs):
    # Eliminar el archivo físico del sistema de archivos
    if instance.imagen_prod:
        # Construye la ruta completa al archivo de imagen
        ruta_archivo = instance.imagen_prod.path

        # Verifica si el archivo existe antes de intentar eliminarlo
        if os.path.exists(ruta_archivo):
            os.remove(ruta_archivo)