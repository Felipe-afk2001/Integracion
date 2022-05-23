from django.shortcuts import render
from rest_framework import serializers, viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import prescripcion
from core.serializers import prescripcionSerializer
# Create your views

class prescripcionViewSet(viewsets.ModelViewSet):
  queryset = prescripcion.objects.all()
  serializer_class = prescripcionSerializer

class prescripcionDetalle(APIView):
  def get(self, request,rut):
    detalle = prescripcion.objects.filter(rut_pac=rut).order_by("-id_presc")
    serializer = prescripcionSerializer(detalle,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)




