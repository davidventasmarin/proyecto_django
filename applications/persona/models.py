from django.db import models
from ckeditor.fields import RichTextField
from applications.departamento.models import Departamento


class Habilidades(models.Model):
    habilidades = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name        = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return self.habilidades

# Create your models here.
class Empleado(models.Model):
    """ Modelo para tabla empleado """
    JOB_CHOICE = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'It'),
        ('3', 'Desarrollador'),
    )

    first_name   = models.CharField('Nombre', max_length=50)
    last_name    = models.CharField('Apellidos', max_length=60)
    full_name    = models.CharField('Nombre Completo', max_length=120, blank=True)
    job          = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar       = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades  = models.ManyToManyField(Habilidades)
    hoja_vida    = RichTextField(null=True)

    class Meta:
        verbose_name_plural = 'Empleado'
        ordering            = ['-last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name