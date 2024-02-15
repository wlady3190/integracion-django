
from django.urls import path

from .views import *

urlpatterns = [
    
    path('listar/', ProfesorListView.as_view(), name='profesor_list'),
    path('crear/', CreateProfesorView.as_view(), name='profesor_create'),
    path('actualizar/<int:pk>', CreateProfesorView.as_view(), name='profesor_update'),
    path('eliminar/<int:pk>', CreateProfesorView.as_view(), name='profesor_delete'),
    
      
    
]