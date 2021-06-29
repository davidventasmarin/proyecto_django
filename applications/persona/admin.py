from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)

# esto sirve para que en el admin me retorne mas cosas des las que 
# le he puesto en el return del modelo
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )

    def full_name(self, obj):
        # toda la operacion que necesites

        return obj.first_name + ' ' + obj.last_name

    # Le dice que por qué campo va a busar cuando escribas algo en el buscador
    search_fields     = ('last_name',)
    # esto es un listado de filtros
    list_filter       = ('departamento', 'job', 'habilidades') 

    filter_horizontal = ('habilidades',) 

admin.site.register(Empleado, EmpleadoAdmin)
