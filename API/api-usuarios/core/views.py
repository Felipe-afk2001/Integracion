from django.shortcuts import render
from rest_framework import serializers, viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Usuario
from core.serializers import UsuarioSerializer
# Create your views

class UsuarioViewSet(viewsets.ModelViewSet):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer

class UserInfoView(APIView):
  def get(self,request,format=None):
    usuario=Usuario.objects.get(usuario=request.user)
    userserializer=UsuarioSerializer(usuario)
    return Response(userserializer.data, status=status.HTTP_200_OK)


