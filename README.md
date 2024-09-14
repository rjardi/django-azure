
Django para principiantes - Microsoft Developer

GitHub: https://github.com/microsoft/beginners-django/tree/main
Youtube: https://youtube.com/playlist?list=PLlrxD0HtieHjHCQ0JB_RrhbQp_9ccJztr&si=W5YpgUUpTv5mkJQ_

1. CONFIGURACIÓN DE ENTORNO 

    1.1. Crear carpeta de proyecto y abrir con VsCode (o IDE)
    1.2. Abrir terminal en vsCode en carpeta de proyecto
    1.3. Crear entorno virtual comando en terminal:
        - python3 -m venv venv
    1.4. Crear archivo requirements.txt en carpeta raiz de proyecto
        - En este archivo definiremos todas las librerias y paquetes que necesitaremos instalar en nuestro entorno virtual para construir nuestro proyecto
        - De momento en este archivo escribiremos una sola linea con:
            django
    1.5. Activar entorno virtual comando en terminal:
        - source ./venv/bin/activate
    1.6. Instalar dependencias de archivo requirements.txt en nuestro entorno virtual:
        - pip install -r requirements.txt
            * La opción -r significa instalar de forma recursiva todo lo que hay indicado en el archivo requirements es decir todas las lineas. En este caso como solo hemos puesto django, de momento, nos instalará el framework.

2. CONCEPTOS DJANGO

    2.1. Django esta basado en pequeñas aplicaciones dentro de nuestro proyecto
    2.2. PROYECTO (PADRE) Primero tenemos nuestro proyecto que por ejemplo engloba toda nuestra web app
    2.3. APLICACIONES (HIJAS) Nuestro proyecto puede tener pequeñas aplicaciones las cuales dan funcionalidad a nuestro proyecto

3. CREAR PROYECTO

    3.1. Escribir en terminal:
        - django-admin startproject [project_name] .
            *Es importante tener en cuenta de poner el . en el final del comando para que se genere en la carpeta actual sino se convierte la estructura en un poco redundante

4. CREAR APLICACION

    4.1. Escribir en terminal:
        - django-admin startapp [app_name]
    4.2. Añadir aplicación en archivo settings.py

5. LEVANTAR SERVIDOR LOCAL

    5.1. Escribir en terminal:
        - python manage.py runserver
            *Recibiremos que tenemos migraciones por realizar pero de momento no le haremos caso

6. VISTAS

    Las vistas son como queremos que los usuarios vean cierta informaición de la base de datos

    6.1. Abrir el archivo views.py en la carpeta de nuestra aplicación para ver el archivo

7. CREAR PRIMERAS URLS

    Las urls se deben crear en archivos separados en cada una de nuestra aplicaciones para tener una mayor claridad y orden en el proyecto

    7.1. Crear archivo llamdo urls.py en la carpeta raiz de nuestra aplicación
    7.2. Añadir los path en la variable urlpatterns en el archivo urls.py de nuestra aplicación
    7.3. Añadir mediante include la referencia al archivo urls de nuestra aplicación en el archivo urls.py general en nuestra carpeta raiz del proyecto.

8. CREAR MODELOS

    En el archivo models.py crearemos los modelos. Los modelos son todas aquellas clases que crearemos las cuales seran equivalentes a tablas o objetos que almacenaremos en la base de datos.

    8.1. Crearemos la clase Destination en el archivo models.py de nuestra aplicación

9. CREAR MIGRACIONES

    9.1. Realizar migraciones de los modelos escribiendo en la terminal:
        - python manage.py makemigrations
            * Esto realizará un paso previo a la migración final creando un archivo migrations dentro de nuestra aplicación con el script de las migraciones que van a realizarse 

    9.2. Realizar migracion definitiva. Escribir en terminal:
        - python manage.py migrate
            * Esto realizará la migración de los modelos a nuestra base de datos. Por defecto la base de datos de django se crea en un archivo dbsqlite. Dbsqlite es un motor de base de datos sencillo el cual no necesita correr servidor ya que se almacena en un archivo local en el proyecto.

    9.3. Para ver los datos de la base de datos, es decir, del archivo que se nos ha creado de db.sqlite3 debemos instalar una extension en vscode llamada SQLite.

        - Si abrimos el archivo vemos que se nos ha creado una tabla o objeto con el nombre nuestra aplicación.nombre_modelo y dentro nos ha puesto los campos que hemos defeinido como clases en el archivo models.py

10. CREAR CONSULTAS CON LA SHELL

    10.1. Escribir en el terminal para abrir la shell:
        - python manage.py shell
    10.2. Importar el modelo deseado de nuestra aplicación:
        - from aplication_name.models import Destination
    10.3. Crear objecto con el listado de todas las instacias de Destinacion:
        - Destination.object.all()
            *Esto nos devolverá una query con todos los objetos de nuestra base de datos del modelo Destination
    10.4. Como actualmente no tenemos ninguna instancia creada creamos una mediante la shell:
        - mars=Destination(name='Mars', description='Red planet', slug='mars')
        - mars.save()
            * Si repetimos el paso anterior ahora nos devolvera el objeto creado
    10.5. Si queremos obtener una instancia de objeto especifico podemos:
        - mars=Destination.objects.get(name='Mars')
            *Esto nos devolvera el objeto existente con el nombre=Mars
    10.6. Actualizar un campo de una instnacia especifica:
        - mars.description='the new description'
        - mars.save()

11. CREAR ADMIN DE SUPERUSUARIO
    
    11.1. Crear supersusuario:
        - python manage.py createsuperuser
    11.2. Levantar runserver y añadir /admin a nuestra url ejemplo: http://127.0.0.1:8000/admin/

12. REGISTRAR LOS MODELOS QUE QUIERO VER EN EL ADMIN SITE

    12.1. Ir al archivo admin.py
    12.3. Definir los modelso que quiero ver escribiendo en el archivo

        from . import models

        # Register your models here.
        admin.site.register(models.Cruise)
        admin.site.register(models.Destination)
    