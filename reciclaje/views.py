from django.shortcuts import render
from .models import Ciudadano, PuntoAcopio

def vista_ciudadano(request):
    ciudadano = Ciudadano.objects.first()
    puntos_acopio = PuntoAcopio.objects.all()

    contexto = {
        'ciudadano': ciudadano,
        'puntos_acopio': puntos_acopio
    }
    return render(request, 'reciclaje/ciudadano.html', contexto)

def canje_recompensas(request):
    return render(request, 'reciclaje/canje.html')

def index(request):
    return render(request, 'reciclaje/inicio.html')

def login_ciudadano(request):
    return render(request, 'reciclaje/login_ciudadano.html')

def login_admin(request):
    return render(request, 'reciclaje/login_admin.html')

def registro_usuario(request):
    return render(request, 'reciclaje/registro.html')