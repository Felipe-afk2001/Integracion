from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class prescripcion(models.Model):
  id_presc = models.AutoField(primary_key=True)
  nom_doc=models.CharField(max_length=50)
  nom_pac=models.CharField(max_length=50)
  rut_pac=models.CharField(max_length=10)
  receta=models.CharField(max_length=500)
  

  


  

