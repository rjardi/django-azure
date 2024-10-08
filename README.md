
# Django para principiantes - Microsoft Developer

GitHub: https://github.com/microsoft/beginners-django/tree/main
Youtube: https://youtube.com/playlist?list=PLlrxD0HtieHjHCQ0JB_RrhbQp_9ccJztr&si=W5YpgUUpTv5mkJQ_

## 1. CONFIGURACIÓN DE ENTORNO 

    - Crear carpeta de proyecto y abrir con VsCode (o IDE)
    - Abrir terminal en vsCode en carpeta de proyecto
    - Crear entorno virtual comando en terminal:
        - python3 -m venv venv
    - Crear archivo requirements.txt en carpeta raiz de proyecto
        - En este archivo definiremos todas las librerias y paquetes que necesitaremos instalar en nuestro entorno virtual para construir nuestro proyecto
        - De momento en este archivo escribiremos una sola linea con:
            django
    - Activar entorno virtual comando en terminal:
        - source ./venv/bin/activate
    - Instalar dependencias de archivo requirements.txt en nuestro entorno virtual:
        - pip install -r requirements.txt
            * La opción -r significa instalar de forma recursiva todo lo que hay indicado en el archivo requirements es decir todas las lineas. En este caso como solo hemos puesto django, de momento, nos instalará el framework.

## 2. CONCEPTOS DJANGO

    - Django esta basado en pequeñas aplicaciones dentro de nuestro proyecto
    - PROYECTO (PADRE) Primero tenemos nuestro proyecto que por ejemplo engloba toda nuestra web app
    - APLICACIONES (HIJAS) Nuestro proyecto puede tener pequeñas aplicaciones las cuales dan funcionalidad a nuestro proyecto

## 3. CREAR PROYECTO

    - Escribir en terminal:
        - django-admin startproject [project_name] .
            *Es importante tener en cuenta de poner el . en el final del comando para que se genere en la carpeta actual sino se convierte la estructura en un poco redundante

## 4. CREAR APLICACION

    - Escribir en terminal:
        - django-admin startapp [app_name]
    -. Añadir aplicación en archivo settings.py

## 5. LEVANTAR SERVIDOR LOCAL

    - Escribir en terminal:
        - python manage.py runserver
            *Recibiremos que tenemos migraciones por realizar pero de momento no le haremos caso

## 6. VISTAS

    Las vistas son como queremos que los usuarios vean cierta informaición de la base de datos

    - Abrir el archivo views.py en la carpeta de nuestra aplicación para ver el archivo

## 7. CREAR PRIMERAS URLS

    Las urls se deben crear en archivos separados en cada una de nuestra aplicaciones para tener una mayor claridad y orden en el proyecto

    - Crear archivo llamdo urls.py en la carpeta raiz de nuestra aplicación
    - Añadir los path en la variable urlpatterns en el archivo urls.py de nuestra aplicación
    - Añadir mediante include la referencia al archivo urls de nuestra aplicación en el archivo urls.py general en nuestra carpeta raiz del proyecto.

## 8. CREAR MODELOS

    En el archivo models.py crearemos los modelos. Los modelos son todas aquellas clases que crearemos las cuales seran equivalentes a tablas o objetos que almacenaremos en la base de datos.

    - Crearemos la clase Destination en el archivo models.py de nuestra aplicación

## 9. CREAR MIGRACIONES

    - Realizar migraciones de los modelos escribiendo en la terminal:
        - python manage.py makemigrations
            * Esto realizará un paso previo a la migración final creando un archivo migrations dentro de nuestra aplicación con el script de las migraciones que van a realizarse 

    - Realizar migracion definitiva. Escribir en terminal:
        - python manage.py migrate
            * Esto realizará la migración de los modelos a nuestra base de datos. Por defecto la base de datos de django se crea en un archivo dbsqlite. Dbsqlite es un motor de base de datos sencillo el cual no necesita correr servidor ya que se almacena en un archivo local en el proyecto.

    - Para ver los datos de la base de datos, es decir, del archivo que se nos ha creado de db.sqlite3 debemos instalar una extension en vscode llamada SQLite.

        - Si abrimos el archivo vemos que se nos ha creado una tabla o objeto con el nombre nuestra aplicación.nombre_modelo y dentro nos ha puesto los campos que hemos defeinido como clases en el archivo models.py

## 10. CREAR CONSULTAS CON LA SHELL

    - Escribir en el terminal para abrir la shell:
        - python manage.py shell
    - Importar el modelo deseado de nuestra aplicación:
        - from aplication_name.models import Destination
    - Crear objecto con el listado de todas las instacias de Destinacion:
        - Destination.object.all()
            *Esto nos devolverá una query con todos los objetos de nuestra base de datos del modelo Destination
    - Como actualmente no tenemos ninguna instancia creada creamos una mediante la shell:
        - mars=Destination(name='Mars', description='Red planet', slug='mars')
        - mars.save()
            * Si repetimos el paso anterior ahora nos devolvera el objeto creado
    - Si queremos obtener una instancia de objeto especifico podemos:
        - mars=Destination.objects.get(name='Mars')
            *Esto nos devolvera el objeto existente con el nombre=Mars
    - Actualizar un campo de una instnacia especifica:
        - mars.description='the new description'
        - mars.save()

## 11. CREAR ADMIN DE SUPERUSUARIO
    
    - Crear supersusuario:
        - python manage.py createsuperuser
    - Levantar runserver y añadir /admin a nuestra url ejemplo: http://127.0.0.1:8000/admin/

## 12. REGISTRAR LOS MODELOS QUE QUIERO VER EN EL ADMIN SITE

    - Ir al archivo admin.py
    - Definir los modelso que quiero ver escribiendo en el archivo

        from . import models

        # Register your models here.
        admin.site.register(models.Cruise)
        admin.site.register(models.Destination)

## 13. FUNCIONES BASADAS EN VISTAS

    - Estas funciones las crearemos en el archivo en la carpeta de nuestra aplicación llamado views.py
    - Estas funciones corresponderan a cada una de las vistas que queremos renderizar y que asociaremos a un archivo plantilla html posteriormente para enviarles las variables del contexto con las cuales queremos trabajar
    - Por ejemplo crearemos dos vistas principales la de la pagina index y about en el archivo views.py de nuestra aplicación

        from django.shortcuts import render

        def index(request):
            return render(request, 'index.html')

        def about(request):
            return render(request, 'about.html')

    - Despues crearemos las correspondientes plantillas html:
        - index.html y about.html

## 14. IMPLEMENTANDO LA LOGICA DE LAS RUTAS
    - Creamos un archivo llamado urls.py en la carpeta de nuestra aplicación (ya lo habiamos hecho previamente)
    - En este archivo definiremos las urlpatterns:

        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.index, name='index'),
            path('about', views.about, name='about'),
        ]
    - Ahora necesitaremos registrarlo en nuestro proyecto en el archivo urls.py principal con la funcion include:

        urlpatterns = [
        path('', include('rgardencloud.urls')),
        path('admin/', admin.site.urls),
        ]   
    - De esta forma le indicamos al archivo principal de urls que estamos estructurando el proyecto en pequeños archivos por aplicación

## 15. PLANTILLAS HTML Y HERENCIA

    - Django permite crear un sistema de plantillas para evitar tener que repetir la escritura de un mismo codigo en diferentes archivos
    - Cada uno de estos archivos se puede heredar de uno o diferentes archivos que ocntengan la información general
    - Despues cada uno de los archivos especificos pueden ir sobreescribiendo la informaicón de estas plantillas base segun convenga
    - Para hacer esto creamos un archivo llamado base.html el cual contenera la información y layout general de la estructura de nuestra apliación o pagina web
    - Dentro del archiov base.html vemos que tenemos un {% funcion %}
    - Esto le indica a djnago que dentro del archivo html tiene que ejecutar un función
    - En el archivo base de html creamos cloques los cuales podremos sobreescribir posteriormente con las plantillas que hereden de esta. Por ejemplo el título de la página:
        <title>
            {% block title %}
            ReleCloud - Expand your horizons
            {% endblock %}
        </title>
    - Después en las plantillas hijas: index.html y about.html sobreescribire este bloque
    - index.html:

        {% extends 'base.html' %}

        {% block title %}
        ReleCloud - Expand your horizons
        {% endblock %}

    - about.html:

        {% extends 'base.html' %}

        {% block title %}
        ReleCloud - About
        {% endblock %}

    - Dentro de las plantillas también indicaremos la ruta de las urls segun hemos definido con la función {% url %}:

        <a class="nav-link" href="{% url 'about' %}">About</a>

## 16. MOSTRAR DATOS DINAMICOS

    - Para mostrar en nuestras plantillas las instancias de los objetos/modelos que hemos creado deberemos crear las funciones en el archivo views.py igual que hemos hecho para index y contact
    - Abrimos el archivo views.py de nuestra aplicación y creamos la vista destinations
    - Enviamos la variable de contexto al renderizar la plantilla llamada destinations con todos los objetos de nuestro modelo
    - Creamos la plantill destinations.html en base a la plantilla base.html
    - Creamos un bucle for mediante funciones de django {% for  in %}{% end for %}
    - Dentro de este bucle creamos una lista no ordenada con cada una de las instancias que contiene nuestro modelo Destination
    - Añadimos la url en el archivo urls
    - referenciamos esta url en el menu de navegación de nuestro archivo base.html para pdoer acceder a esta vista

## 17. MOSTRAR VISTAS GENERALES DE NUESTROS MODELOS

    - Django nos permite crear las tipicas vistas: Detalle, Crear, Eliminar, Editar.
    - Esto se realiza mediante las clases bsadas en vistas de modelos
    - Creamos en el archivo views las vistas que heredaran del paquete generic de django 
    - Creamos las plantillas html asociadas a cada vista: destination_form.html (la usaremos para update y create), destination_confirm_delete.html.
    - Después asociaremos estas vistas a cada una de las urls
    - Las urls update, delete i detail tendran como parametro el id del modelo en la url
    - Sobreescribiremos en la clase del modelo Destination el metodo get_absolute_url para que nos devuelva siempre la vista detalle de la isntancia en cuestión al hacer la petición 

## 18. VISTAS GENERICAS CON DJANGO-CRISPY-FORMS

    - django-crispy forms es una libreria que se utiliza para dar un mejor formato a nuestros formularios ya que por defecto los formularios via la funcion {{form.as_p}} se renderizan de forma un poco desorganizada
    - Para utilizarlo instalamos el paquete en nuestro entorno virtual:
        pip install django-crispy-forms
    - Instalamos el paquete de estilo deaseado por ejemplo el crispy-bootstrap4
        pip install crispy-bootstrap4
    - Añadimos las aplicaciones en settings.py según: https://django-crispy-forms.readthedocs.io/en/latest/install.html:
        INSTALLED_APPS = [
            '.......',
            'crispy_forms',
            'crispy_bootstrap4'
        ]
    - Añadimos la variable CRISPY_TEMPLATE_PACK en settings.py:
        CRISPY_TEMPLATE_PACK = 'bootstrap4'
        
    - Añadimos en la plantilla html del formulario el load y el filtro de crispy:

        {% load crispy_forms_tags %}

        {{ form|crispy }}

## 19. AÑADIR POSTGRES COMO BASE DE DATOS

    - La base de datos de sqlite normalmente es para hacer pruebas ya que al ser un archivo cada vez que hagamos el deploy en azure se sobreescribirá
    - Una opción más escalable es usar un servidor de base de datos como postgres el cual es ofrecido en azure
    - Vamos a la extensión de azure y clicamos en el icono '+' ubicado al lado de resources arriba de todo
    - Seleccionamos 'Create database Server'
    - Seleccionamos 'PostgreSQL Single Server'
    - Introducimos el nombre identificativo de nuestra base de datos ejemplo: [app_name-db]
    - Seleccionar additional options en los planes de precios
    - Introducir nombre de administrador
    - Introducir contraseña
    - Seleccionar mismo recurso creado de nuestra web app
    - Esperar que se cree
    - Una vez creado, vamos al portal web de azure y en la pagina de inicio ponemos en el buscador postgres.
    - Seleccionamos la opción de 'Servidores de Azure Database for PostgreSQL'
    - Nos saldra la database que acabamos de crear en el listado, seleccionamos.
    - Vamos a configuración > Seguridad de la conexión
    - Seleccionar en Añadir la IP del cliente actual (La nuestra)
    - Activamos el 'Permitir el acceso a servicios de Azure'
    - Le damos a Guardar

    - Modificar el archivo settings.py de nuestro proyecto y modificar la propiedad DATABASES:
        
        DATABASES = {
            'default': {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": "mydatabase",
                "USER": "[mydatabaseuser]",
                "PASSWORD": os.getenv("[DB_PASSWORD]"),
                "HOST": "[mydatabase_name]",
                "PORT": "5432",
                "OPTIONS": {'sslmode': 'require'},
            }
        }
    
    - Los valores entre [] se obtienen del portal sección Información general
    - Vamos a la extensión>RESOURCES>Azure subscription X>PostgreSQL servers>database_name
    - Clicar con el derecho en el recurso con el nombre de nuestra base de datos y seleccionar Create Database
    - Poner el nombre que hemos definido en settings.py en la propiedad NAME de DATABASE
    - Instalar en nuestro venv la dependencia psycopg2-binary:
        pip install psycopg2-binary
    - Añadir a archivo requirements.txt:
        pip freeze > requirements.txt
    - Definir la variable DB_PASSWORD desde el terminal
        - Desde MAC/Linux:
            export DB_PASSWORD=[db_password]
        - Deste Windows:
            set DB_PASSWORD=[db_password]
    - Realizar migraciones:
        python3 manage.py migrate
    - Si Sale el mensaje de error "django.db.utils.NotSupportedError: PostgreSQL 13 or later is required (found 11.22)." Es porque la vesrión del PostgreSQL server es la 11 y se debe hacer downgrade de django a la versión 4.1
    - Deberemos desinstalar las dependencias que nos den error con el downgrade. Por ejemplo crispy-forms, psycopg
    - Tambien deberemos hacer los siguientes downgrades para que nos quede en requirements.txt:
        crispy-bootstrap4==2022.1
        Django==4.1
        django-crispy-forms==2.0
        psycopg2-binary==2.9.9
    - Realizar migraciones:
        python3 manage.py migrate
    - Ahora deberia funcionar!

    - Añadir la variable DB_PASSWORD en extension de azure.
    - Clicar con derecho encima de aplication settings en nuestra app service y añadir nueva setting:
        DB_PASSWORD=[password]

    -  Finalmente hacer deploy to web app clicando con derecho encima de nuestra web app service

    - Solamente faltaria crear el superusuario para la neuva base de datos con el comando:
        python manage.py createsuperuser
    - Ya podremos acceder al panel de /admin de nuestra app en producción con nuestras credenciales

    ### - Y ya lo tendriamos!!!!

    

















    