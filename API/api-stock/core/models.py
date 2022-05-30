from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class medicamento(models.Model):
  id_stock = models.AutoField(primary_key=True)
  nom_drug = models.CharField(max_length=50)
  descripcion = models.CharField(max_length=200)
  max_cant = models.IntegerField(blank=True)
  laboratorio = models.CharField(max_length=50)

  

