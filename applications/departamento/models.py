from django.db import models

# Create your models here.
class Departamento(models.Model):
    name      = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate   = models.BooleanField('Anulado', default=False)

    # para modificar el nombre que aparecerá en admin
    class Meta:
        verbose_name        = 'Mi Departamento'
        # cuando hayan varios registros
        verbose_name_plural = 'Área de la empresa'
        # para que se ordene en admin por nombre
        ordering            = ['name']
        # evita que puedas introducir una combinación de campos
        unique_together     = ('name', 'shor_name')

    def __str__(self):
        return self.shor_name