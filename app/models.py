from django.db import models

class Efemeride(models.Model):
    fecha = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.fecha} - {self.descripcion}'
