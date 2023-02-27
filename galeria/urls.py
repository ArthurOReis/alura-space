from django.urls import path, include
from galeria.views import *

urlpatterns = [
    path('', index, name='index'),
    path('imagem', imagem, name='imagem'),
]