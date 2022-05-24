from django.shortcuts import render
from rest_framework import serializers, viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import medicamento
from core.serializers import medicamentoSerializer
# Create your views

class medicamnetoViewSet(viewsets.ModelViewSet):
  queryset = medicamento.objects.all()
  serializer_class = medicamentoSerializer

class medicamentoDetalle(APIView):
  def get(self, request,id):
    detalle = medicamento.objects.filter(id_stock=id).order_by("-id_stock")
    serializer = medicamentoSerializer(detalle,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)




