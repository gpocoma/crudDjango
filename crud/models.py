from django.db import models

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=512)
    apellido_paterno = models.CharField(max_length=512)
    apellido_materno = models.CharField(max_length=512)
    ci = models.IntegerField()
    nit = models.IntegerField()
    telefono = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.nombre} - {self.apellido_paterno} - CI: {self.ci}'

