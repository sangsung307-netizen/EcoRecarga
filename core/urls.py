from django.contrib import admin
from django.urls import path, include
from reciclaje import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ciudadano/', views.vista_ciudadano, name='vista_ciudadano'),
    path('canje/', views.canje_recompensas, name='canje_recompensas'),
    path('administrador/', include('administrador.urls')),
]