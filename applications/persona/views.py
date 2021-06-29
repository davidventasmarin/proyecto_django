from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Empleado
from django.http import HttpResponseRedirect

# Create your views here.
# 1.- Listar todos los empleados de la empres
# 2.- Listar todos los empleados que pertenecen a un área de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar habilidades de un empleado.

class InicioView(TemplateView):
    """ Pagina que carla la página de inicio """
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name       = 'persona/listado_all.html'
    paginate_by         = 4
    ordering            = 'last_name'
    model               = Empleado
    context_object_name = 'lista'
    
class ListByArea(ListView):
    """ LIsta empleados por area"""
    template_name               = 'persona/listado_by_area.html'
    model                       = Empleado
    context_object_name         = 'listaByArea'
   
    # Con esto podemos hacer filtros de un ListView con get_queryset
    def get_queryset(self):

        area  = self.kwargs['shorname']
        lista = Empleado.objects.filter(
        departamento__shor_name = area
        )

        return lista

class ListByTrabajo(ListView):
    """ LIsta empleados por area"""
    template_name       = 'persona/listado_by_trabajo.html'
    model               = Empleado
    context_object_name = 'listaByTrabajo'
   
    # Con esto podemos hacer filtros de un ListView con get_queryset
    def get_queryset(self):

        area  = self.kwargs['job']
        lista = Empleado.objects.filter(
        job=area
        )

        return lista

class ListEmpleadoByKword(ListView):
    """ Lista empleado por palabra clave """
    template_name       = 'persona/by_kword.html'
    context_object_name = 'empleado'

    def get_queryset(self):
        # el espacio del final es por que lo que devuelve GET es una lista
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name       = 'persona/list_habilidades_empleado.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        """
        La lógica que estamos escribiendo aquí, viene dada de que 
        nosotros queremos sacar la lista de habilidades, las habilidades
        tienen una relación manytomany con empleado, ya que un empleado
        puede tener muchas habilidades y una habilidad pertenece a muchos
        empleado, por lo tanto primero nosotros queremos obtener un empleado
        por el id ya que no se va a repetir nunca, y luego, sacar las 
        habilidades de ese empelado.
        """
        id_empleado = self.kwargs['id']
        empleado    = Empleado.objects.get(
            id=id_empleado
        )
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    # necesitamos el modelo por que es lo que vamos a imprimir
    model               = Empleado
    template_name       = "persona/detail_empleado.html"
    # Lo podemos nombrar de esta forma como antes, o también
    # sin poner nada aquí y referenciando al modelo en este caso
    # Empleado
    # context_object_name = "detalleEmpleado"

    def get_context_data(self, **kwargs):
        context           = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes' 
        return context

class SuccessView(TemplateView):
    template_name = "persona/success.html"   

class EmpleadoCreateView(CreateView):
    model         = Empleado    
    template_name = "persona/add.html"
    # fields        = ('__all__') # Para añadir todos los campos
    fields        = [
        'first_name' , 
        'last_name', 'job',
        'departamento',
        'habilidades',
        ]
    #success_url   = '.' lo ponemos así si queremos que vaya a la misma pantalla
    success_url   = reverse_lazy('persona_app:correcto')

    def form_valid(self, form):
        # Lógica del proceso (Con los datos insertados, creamos el full name)
        empleado           = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save() 
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model         = Empleado
    template_name = "persona/update.html"
    fields        = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url    = reverse_lazy('persona_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model         = Empleado
    template_name = "persona/delete.html"
    success_url   = reverse_lazy('persona_app:correcto')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
