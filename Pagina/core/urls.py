from django.urls import path
from .views import index,obras,autores,login,chicagogaleria,Autor,categoria,load, registrarse

urlpatterns = [
    path('',index,name="index"),
    path('obras/<id>',obras,name="obras"),
    path('categorias/<id>',categoria,name="categorias"),
    path('autores/',autores,name="autores"),
    path('login/',login,name="login"),
    path('chicagogaleria/',chicagogaleria,name="chicagogaleria"),
    path('autor/<id>',Autor,name="autor"),
    path('load/',load,name="load"),
    path('Registrarse/',registrarse,name="Registrarse"),
]
