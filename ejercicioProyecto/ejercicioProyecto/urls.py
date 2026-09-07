"""
URL configuration for ejercicioProyecto project.
"""
from django.contrib import admin
from django.urls import path
from ejercicioApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', miTienda, name='miTienda'),
    path('electronica/', electronica, name='electronica'),
    path('jugueteria/', jugueteria, name='jugueteria'),
    path('ropa/', ropa, name='ropa'),
    path('producto/<int:id_producto>/', detalleProducto, name='detalle'),
]
