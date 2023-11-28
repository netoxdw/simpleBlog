from django.shortcuts import render
# Importando las vistas genericas
from django.views import generic
# Importando modulo para crear usuarios
from django.contrib.auth.forms import UserCreationForm
# Redireccionar al usuario creado
from django.urls import reverse_lazy



# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')