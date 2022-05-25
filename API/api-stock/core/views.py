from ast import IsNot
from urllib import response
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import serializers, viewsets, status,generics
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import medicamento
from core.serializers import medicamentoSerializer
# Create your views


class medicamentoDetalle(generics.ListAPIView):
  serializer_class=medicamentoSerializer
  def get_queryset(self):
    queryset=medicamento.objects.all()
    id=self.request.query_params.get("id_stock")
    nom=self.request.query_params.get("nom_drug")
    if id is not None:
      queryset=queryset.filter(id_stock=id)
    if nom is not None:
      queryset=queryset.filter(nom_drug=nom)
    return queryset
class actualizarMedicamento(APIView):
  def get_object(self, id):
    return medicamento.objects.get(id_stock=id)
  def patch(self, request,id):
    objeto=self.get_object(id)
    serializer=medicamentoSerializer(objeto,data=request.data,partial=True)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(data=serializer.data,status=201)
    return JsonResponse(data="Datos invalidos",status=400)
  def delete(self,request,id):
     objeto=self.get_object(id)
     objeto.delete()
     return Response(status=status.HTTP_204_NO_CONTENT)


