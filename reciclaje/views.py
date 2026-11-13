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