from django.shortcuts            import render
from django.urls                 import reverse_lazy
from django.views.generic.edit   import FormView
from .forms                      import NewDepartamentoForm
from applications.persona.models import Empleado
from .models                     import Departamento
                     
# Create your views here.

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class    = NewDepartamentoForm
    success_url   = '/'

    def form_valid(self, form):
        print('*** Esto es el form valid ***')
        # crear una instancia de departamento por que es clave ajena
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname']
        )
        depa.save()

        nombre   = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )
        return super(NewDepartamentoView, self).form_valid(form)
