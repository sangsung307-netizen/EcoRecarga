from django.contrib import admin
from django.urls import path, include
from reciclaje import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ciudadano/', views.vista_ciudadano, name='vista_ciudadano'),
    path('canje/', views.canje_recompensas, name='canje_recompensas'),
    path('administrador/', include('administrador.urls')),
    path('', views.index, name='inicio'),
    path('login/ciudadano/', views.login_ciudadano, name='login_ciudadano'),
    path('login/', views.login_admin, name='login_admin'),
    path('registro/', views.registro_usuario, name='registro'),
   
]