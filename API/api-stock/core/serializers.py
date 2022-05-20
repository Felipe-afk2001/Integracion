from rest_framework import serializers
from core.models import medicamento
from django.contrib.auth import get_user_model

class medicamentoSerializer(serializers.ModelSerializer):
  # tipoUsuario = serializers.HyperlinkedRelatedField(view_name="tipousuario-detail", read_only=True)
  class Meta:
    model = medicamento
    fields = '__all__'


