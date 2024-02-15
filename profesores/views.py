from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
# Create your views here.
from django.shortcuts import render
import requests

from profesores.models import Profesor




class CreateProfesorView(CreateView):
    template_name='profesor_form.html'
    model= Profesor
    context_object_name= 'profesor_data'
    fields= ['nombre', 'apellido', 'materia', 'correo']
    success_url = reverse_lazy('maestro_list')
    
    def form_valid(self, form):
        # Realizar una solicitud POST a la API con los datos del formulario
        response = requests.post('http://localhost:9091/profesores', data=form.cleaned_data)
        return super().form_valid(form)
    
class ProfesorListView(ListView):
    model=Profesor
    fields= ['nombre', 'apellido', 'materia', 'correo']
    template_name= 'profesor/profesor_list.html'
    context_object_name= 'profesor_data'
    
    def get_queryset(self):
        # Realizar una solicitud GET a la API y devolver los datos
        response = requests.get('http://localhost:9091/profesores')
        print(response)
        return response.json()
    
    
    
    
    