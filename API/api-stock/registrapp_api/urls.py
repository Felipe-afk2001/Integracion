"""registrapp_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core import views
from core.views import medicamentoDetalle,actualizarMedicamento

router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('medicamento/', medicamentoDetalle.as_view(), name="medicamento"),
    path('medicamento/<int:id>/', actualizarMedicamento.as_view(), name="medicamento"),
    path('', include(router.urls)),
]
