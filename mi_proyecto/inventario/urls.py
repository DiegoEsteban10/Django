from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.cursoLista, name='curso_listado'),
    path('items/<int:pk>', views.cursoDetalle, name='curso_detalle'),
    path('items/nuevo/', views.cursoNuevo, name='curso_nuevo'),
    path('items/<pk>/editar/', views.cursoEditar, name='curso_editar'),
    path('items/<pk>/eliminar/', views.cursoEliminar, name='curso_eliminar'),
    
]