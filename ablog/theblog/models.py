from django.db import models
# Investigar para que se usa. Al parecer es para conectar con superuser y usuarios creados
from django.contrib.auth.models import User
# Importar metodo reverse
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=100, default='Este es un post')
    # Esto quiere decir on_delete=models.CASCADE que se se elimina al usuario que escribio el post en automatico se eliminan sus posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    # Investigar como se llama esta funcion   
    # El str(self.author) se encapsula por ser un objeto foraneo
    def __str__(self):
        return self.title + ' | ' + str(self.author) 
    
    class Meta:
        ordering = ['-post_date']

        
    def get_absolute_url(self):
        return reverse('index')
