from django.shortcuts import render, redirect
from .forms import ProfesorForm, EstudianteForm, CursoForm
from .models import Estudiante, Profesor, Curso


# Vista para crear un profesor
def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo profesor en la base de datos
            return redirect('inicio')  # Redirigir a la vista de inicio después de guardar
    else:
        form = ProfesorForm()  # Crear un formulario vacío si la solicitud no es POST
    return render(request, 'appKim/profesor.html', {'form': form})

# Vista para crear un estudiante
def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo estudiante en la base de datos
            return redirect('inicio')  # Redirigir a la vista de inicio después de guardar
    else:
        form = EstudianteForm()  # Crear un formulario vacío si la solicitud no es POST
    return render(request, 'appKim/estudiantes.html', {'form': form})

# Vista para crear un curso
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo curso en la base de datos
            return redirect('inicio')  # Redirigir a la vista de inicio después de guardar
    else:
        form = CursoForm()  # Crear un formulario vacío si la solicitud no es POST
    return render(request, 'appKim/cursos.html', {'form': form})

# Vista para la página de inicio
def inicio(request):
    return render(request, 'appKim/inicio.html')

#Busquedad 
# views.py




def buscar(request):
    query = request.GET.get('query', '')
    resultados_estudiantes = Estudiante.objects.filter(nombre__icontains=query)
    resultados_profesores = Profesor.objects.filter(nombre__icontains=query)
    resultados_cursos = Curso.objects.filter(nombre__icontains=query)

    return render(request, 'appKim/buscar.html', {
        'query': query,
        'resultados_estudiantes': resultados_estudiantes,
        'resultados_profesores': resultados_profesores,
        'resultados_cursos': resultados_cursos,
    })
