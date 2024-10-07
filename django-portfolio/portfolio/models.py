from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/images")
    url = URLField(blank=True)
    

class Experiencia(models.Model):
    institucion_del_curso = models.CharField(max_length=255)
    descripcion_curso = models.TextField()
    fecha_curso = models.DateField()
    numero_horas = models.IntegerField()

    def __str__(self):
        return f'{self.descripcion_curso} - {self.institucion_del_curso}'

class Educacion(models.Model):
    titulo = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    anio_inicio = models.PositiveIntegerField(default=2000)  # Valor por defecto para evitar el error
    anio_fin = models.PositiveIntegerField(default=2004)  # Valor por defecto para evitar el error
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo