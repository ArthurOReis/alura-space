from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')), # Em galeria, é criado 'urls.py' para se responsabilizar em criar outras páginas,
]
