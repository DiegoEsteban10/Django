from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoForm
from django.contrib import messages
from datetime import date
from django.urls import reverse
from django.views.decorators.http import require_POST

def curso_eliminar(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        messages.success(request, "Curso eliminado correctamente.")
        return redirect('curso_listado')
    return render(request, 'cursos/eliminar_confirmacion.html', {'curso': curso})


# Create your views here.

def cursoLista(request):
    q = request.GET.get('q', '')
    sort = request.GET.get('sort', 'nombre')
    cursos = Curso.objects.all()
    
    if q:
        cursos = cursos.filter(nombre__icontains=q)   
        
    cursos = cursos.order_by(sort)
    
    paginator = Paginator(cursos, 5)
    page = request.GET.get('page')
    cursos_page = paginator.get_page(page)
    
    context = {
        'cursos': cursos_page,
        'q': q,
        'sort': sort
    }
    return render(request, 'cursos/listado.html', context)




def cursoDetalle(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'cursos/detalle.html', {'curso': curso})


def cursoNuevo(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso creado correctamente.')
            return redirect('curso_listado')
    else:
        form = CursoForm()
    return render(request, 'cursos/formulario.html', {'form': form, 'modo': 'Nuevo', 'today': date.today().isoformat()})


def cursoEditar(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso actualizado correctamente.')
            return redirect('curso_listado')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/formulario.html', {'form': form, 'modo': 'Editar', 'today': date.today().isoformat()})



def cursoEliminar(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        messages.success(request, "Curso eliminado correctamente.")
        return redirect('curso_listado')
    return render(request, 'cursos/eliminar.html', {'curso': curso})