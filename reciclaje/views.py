from django.shortcuts import redirect, render
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
    if request.method == 'POST':
        # Por ahora te redirige directo a la interfaz del ciudadano al enviar el formulario
        return redirect('vista_ciudadano')
    
    return render(request, 'reciclaje/login_ciudadano.html')

def login_admin(request):
    if request.method == 'POST':
        # Por ahora te redirige directo a la ruta del panel de administrador
        return redirect('/administrador/')
    return render(request, 'reciclaje/login_admin.html')

def registro_usuario(request):
    return render(request, 'reciclaje/registro.html')