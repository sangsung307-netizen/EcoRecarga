from django.db import models

# 1. Tabla de Usuarios
class Ciudadano(models.Model):
    carnet = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    puntos_acumulados = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} ({self.carnet})"

# 2. Tabla de las sucursales de reciclaje
class PuntoAcopio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    horario = models.CharField(max_length=100)
    materiales_aceptados = models.CharField(max_length=200) 

    def __str__(self):
        return self.nombre

# 3. Tabla del registro de pesaje (admin)
class RegistroReciclaje(models.Model):
    MATERIALES = [
        ('PL', 'Plastico (PET)'),
        ('AL', 'Aluminio'),
        ('VI', 'Vidrio'),
        ('PA', 'Papel y Carton'),
    ]
    
    ciudadano = models.ForeignKey(Ciudadano, on_delete=models.CASCADE)
    punto_acopio = models.ForeignKey(PuntoAcopio, on_delete=models.SET_NULL, null=True)
    material = models.CharField(max_length=2, choices=MATERIALES)
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2)
    puntos_otorgados = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.peso_kg}kg de {self.get_material_display()} - {self.ciudadano.nombre}"

# 4. Tabla del catalogo de premios disponibles
class Recompensa(models.Model):
    nombre = models.CharField(max_length=100)
    costo_puntos = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.costo_puntos} pts)"

# 5. Tabla para guardar cuando alguien cambia sus puntos por un premio
class CanjeRecompensa(models.Model):
    ciudadano = models.ForeignKey(Ciudadano, on_delete=models.CASCADE)
    recompensa = models.ForeignKey(Recompensa, on_delete=models.CASCADE)
    fecha_canje = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ciudadano.nombre} canjeó {self.recompensa.nombre}"