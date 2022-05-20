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




