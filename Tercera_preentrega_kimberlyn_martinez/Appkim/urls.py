from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),  # URL: Appkim/inicio/
    path('crear-profesor/', views.crear_profesor, name='crear_profesor'),  # URL: Appkim/crear-profesor/
    path('crear-estudiante/', views.crear_estudiante, name='crear_estudiante'),  # URL: Appkim/crear-estudiante/
    path('crear-curso/', views.crear_curso, name='crear_curso'),  # URL: Appkim/crear-curso/
    path('buscar/', views.buscar, name='buscar'),
]
