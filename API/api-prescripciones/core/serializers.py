from rest_framework import serializers
from core.models import prescripcion
from django.contrib.auth import get_user_model

class prescripcionSerializer(serializers.ModelSerializer):
  # tipoUsuario = serializers.HyperlinkedRelatedField(view_name="tipousuario-detail", read_only=True)
  class Meta:
    model = prescripcion
    fields = '__all__'


