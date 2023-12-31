# Guía para crear simpleBlog

En este tutorial podras conseguir paso a paso una guia para instalar y crear un blog con Django. Aprenderas a crear un blog donde podras crear, leer, actualizar y eliminar datos. 


El procedimiento esta dividido en sesiones grabadas de youtube.

#### Set Up.

* Terminal (windows ó bash).
* Editor de código  (Visual Studio Code).
* Navegador (Chrome).


## Video 1: Crear un blog con python django.

### Paso 1: Crea un repositorio (carpeta).

Crea un repositorio con el nombre que sea adecuado para tu proyecto, en este caso la nombraremos simpleBlog.

```
mkdir simpleblog
```

Nos direccionamos al repositorio creado.

```
cd simpleblog
```

### Paso 2: Virtualización.

Cuando trabajamos con django es una buena practica crear un entorno virtual donde instalaremos las librerías con diferentes versiones sin que entren en conflicto con los demás entornos.

* Crear el entorno virtual 
```
python -m venv virtualenv
```

La palabra "virtualenv" es el nombre que le queremos poner a nuestro entorno virtual, por lo que tú lo puedes cambiar a tu preferencia. 

### Paso 3: Activar entorno virtual.

Activar el entorno virtual es indispensable para comenzar a trabajar, recuerda activar tu entorno virtual cada vez que trabajes con tu proyecto y tampoco olvides desactivarlo cuando vas a descansar de tu día laboral.

* Comando básico para activación.
```
.\virtualenv\Scripts\activate
```

Si es la primera vez que creas un entorno virtual en tu ordenador es probable que te topes con un error y esto se soluciona activando los scripts de Windows. Para solucionarlo hay muchos recursos en la red que te pueden ser útiles. Prueba buscando activar scripts en Windows.

### Paso 4: Instalar django.

* Comando para instalar django.
```
pip install django
```

* Asegurate de que django se instalo correctamente.
```
pip freeze
```

* Guarda las librerias y versiones en un archivo de requerimeintos.
```
pip freeze > requeriments.txt 
```

### Paso 5: Crear proyecto.

* Comando para crear nuestro proyecto 
```
django-admin startproject aBlog
```
Donde aBlog es el nombre de nuestro proyecto, este lo puedes cambiar por el que te apetezca. 

* Nos direccionamos a nuestro proyecto aBlog
```
cd aBlog
```

* Si asi lo deseas, puedes ejecutar el servidor y ver como tu proyecto ya funciona (opcional).
```
python manage.py runserver
```
* Para cerrar la ejecución del servidor oprime control + c en tu terminal.


### Paso 6: Crear super usuario.

Antes de crear un super usuario en django debemos migrar la base de datos que trae por defecto django.

* Migraciones.
```
python manage.py migrate
```

Estamos listos para crear un super usuario.

* Superuser
```
python manage.py createsuperuser
```
No olvides cual fue el usuario y contraseña. Las usaras a lo largo del proyecto.

### Paso 7: Crear aplicación.

* Comando para crear aplicación.
```
python manage.py startapp theblog
```
theblog es el nombre de nuestra aplicación. La puedes cambiar si así lo deseas.

* Agrega el nombre de la aplicación en el archivo settings.py, busca la sección Intalled_apps.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'theblog',
]
```
#### Paso 7.2: Mapear la url de nuestra aplicación.

En el archivo ubicado en ablog/urls.py debemos importar el modulo include y mapear la url de nuestra aplicación.
* Ejemlo.

```python
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
]
```

Crear archivo urls.py dentro de nuestra aplicación theblog/urls.py e importamos el path

```python
from django.urls import path

```

### Paso 8: Vistas de mi aplicación.

Dentro de la apliacación theblog crearemos un repositorio llamado templates, donde crearemos un archivo llamado index.html.

Es importante saber que en este proyecto utilizaremos las vistas genericas que trae por defecto django.

* En nuestro endpoint views.py que se ubica en theblog/views.py crearemos una vista basada en clase. 
```python
# En esta linea se estan importando las vistas genericas de django
from django.views.generic import ListView

# La funcion indexView es exportada a urls.py de la apliación
class IndexView(ListView):
    model = Post
    template_name = 'index.html' 
```
* En endpoitn urls.py que se ubica en theblog/urls.py 

```python
# Importar la clase creada en vews.py llamada IndezView
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # Las comillas: indican que sera nuestra url, en este caso estan vacias porque sera la pagina de inicio.
    # IndexView es la clase que importamos de las vistas y le estamos indicando que la considere como una vista.
    # name: indica el nombre del archivo que vamos a renderizar, se ubica dentro de nuestra carpeta de templates.  
]
```
### Paso 9: Modelos.

En django un modelo es la representación de nuestra base de datos, lo cual nos facilita demasiado el trabajo.

* En endpoint ubicado en theblog/models.py creamos nuestro objeto.
```py
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=100, default='Este es un post')
    # Esto quiere decir on_delete=models.CASCADE que se se elimina al usuario que escribio el post en automatico se eliminan sus posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author) 
```
* Importamos el modelo que viene por defecto con django admin, donde creamos a nuestros usuarios
```py
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=100, default='Este es un post')
    # Esto quiere decir on_delete=models.CASCADE que se se elimina al usuario que escribio el post en automatico se eliminan sus posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author) 
```

* Le tenemos que decir a django admin que hemos creado un modelo, por lo que debemos ir a nuestro archivo admin.py dentro de theblog.

* Importamos en modelo Post.
```py
from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)
```

### Paso 10: Migrar los modelos a la base de datos.

Cada que modificamos los modelos debemos hacer migraciones a la base de datos con dos comandos.
* El primero
```
python manage.py makemigrations
```

* El segundo
```
python manage.py migrate
```


##### Genial ya tenemos un gran avance. 
No olvides desactivar el entorno virtual dentro de simpleblog/


```
Deactivate
```





