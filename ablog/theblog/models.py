from django.db import models
# Investigar para que se usa. Al parecer es para conectar con superuser y usuarios creados
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    # Esto quiere decir on_delete=models.CASCADE que se se elimina al usuario que escribio el post en automatico se eliminan sus posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    # Investigar como se llama esta funcion   
    # El str(self.author) se encapsula por ser un objeto foraneo
    def __str__(self):
        return self.title + ' | ' + str(self.author) 