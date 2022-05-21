from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
  usuario = models.OneToOneField(User, on_delete=models.CASCADE)
  run = models.CharField(max_length=10, primary_key=True)
  tipo_usuario =models.CharField(max_length=1)

  def __str__(self):
    return f"{self.usuario.username}"


  
