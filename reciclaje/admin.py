from django.contrib import admin
from .models import Ciudadano, PuntoAcopio, RegistroReciclaje, Recompensa, CanjeRecompensa

admin.site.register(Ciudadano)
admin.site.register(PuntoAcopio)
admin.site.register(RegistroReciclaje)
admin.site.register(Recompensa)
admin.site.register(CanjeRecompensa)