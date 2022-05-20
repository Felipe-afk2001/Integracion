from rest_framework import serializers
from core.models import Usuario
from django.contrib.auth import get_user_model

class UsuarioSerializer(serializers.ModelSerializer):
  # tipoUsuario = serializers.HyperlinkedRelatedField(view_name="tipousuario-detail", read_only=True)
  class Meta:
    model = Usuario
    fields = '__all__'


