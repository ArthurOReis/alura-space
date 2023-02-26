from django.contrib import admin
from django.urls import path
from galeria.views import index #Importa a função view que faz retorno de uma requisição HTTP

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index) #Cria uma rota e o que retornar com a sua requisição
]
