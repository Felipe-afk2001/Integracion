from django.db import models

# Create your models here.
class categorias(models.Model):
    id_categoria=models.IntegerField(primary_key=True, verbose_name='id de la categoria')
    nombrec=models.CharField(max_length=50, verbose_name='nombre de la categoria')
    imagen=models.CharField(max_length=1000, verbose_name='imagen categoria')
    def __str__(self):
        return self.nombrec

class autor(models.Model):
    id_autor=models.IntegerField(primary_key=True, verbose_name='id del autor')
    nombrea=models.CharField(max_length=50, verbose_name='nombre del autor')
    descripcion=models.CharField(max_length=2500, verbose_name='descripcion del autor')
    imagen=models.CharField(max_length=1000, verbose_name='imagen autor')
    categorias=models.ForeignKey(categorias,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombrea

class obras(models.Model):
    id_obra=models.IntegerField(primary_key=True,verbose_name='id de la obra')
    nombreo=models.CharField(max_length=50, verbose_name='nombre de la obra')
    descripcion=models.CharField(max_length=2500, verbose_name='descripcion de la obra')
    imagen=models.CharField(max_length=1000, verbose_name='imagen obra')
    precio=models.IntegerField(verbose_name='precio de la obra')
    autor=models.ForeignKey(autor, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombreo

