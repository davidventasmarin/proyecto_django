from django.contrib import admin
from django.urls import path

from . import views

app_name    = "persona_app"
 
urlpatterns = [
    path('', views.InicioView.as_view()),
    path(
        'list_all/', 
        views.ListAllEmpleados.as_view(),
        name='empleados_all'),
    path('list_by_area/<shorname>', views.ListByArea.as_view()),
    path('list_by_trabajo/<job>', views.ListByTrabajo.as_view()),
    path('list_by_kword/', views.ListEmpleadoByKword.as_view()),
    path('list_habilidades/<id>', views.ListHabilidadesEmpleado.as_view()),
    #pk siempre va a ser primary key
    path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view()),
    path('add-empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar-empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado')
]