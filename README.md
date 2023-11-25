# Guia para crear simpleBlog

En esta guia puedes encontrar los pasos que debes seguir para crear un blog con el Framework Django, así como los comandos necesarios.

El procedimiento se dividide en sesiones grabadas de youtube.

#### Set Up.

* Terminal (windows ó bash).
* Editor de codigo (Visual Studio Code).
* Navegador (Chroome).


## Video 1. Crear un blog con python django.

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

La palabra "virtualenv" es el nombre que le queremos poner a nuestro entorno virual, por lo que tú lo puedes cambiar a tu preferencia. 

### Paso 3: Activar entorno virtual.

Activar el entorno virtual es indispensable para comenzar a trabajar, recuerda activar tu entorno virtual cada vez que trabajes con tu proyecto y tampoco olvides desactivarlo cuando vas a descansar de tu dia laboral.

* Comando basico para activación.
```
.\virtualenv\Scripts\activate
```

Si es la primera vez que creas un entorno virtual en tu ordenador es probable que te topes con un error y esto se soluciona activando los scripts de windows. Para solucionarlo hay muchos recursos en la red quee te pueden ser utiles. Prueba buscando activar scripts en windows. 

### Paso 4: Instalar django.

```
pip install django
```

