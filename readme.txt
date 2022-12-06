IMPORTANTE: Necesario usar python 3.9+ (por cosas de django con la bd)
    en caso de usar una versión menor : https://code.djangoproject.com/wiki/JSON1Extension 
1) para crear entorno virtual con python (RECOMENDADO) (en consola):
    python -m venv env
    "python" reemplazable por el comando que usa tu versión (e.g. py, python3, py3, etc)
    "env" es el directorio que se crea el entorno virtual.

    1.1) Ejecutar entorno virtual:
        Windows: env/Scripts/activate
    1.2) salir del entorno virtual:
        deactivate

Recomendado hacer todo en el entorno virtual.
2)Instalar requerimientos:
    (en directorio con requirements.txt)
    pip install -r requirements.txt

Para ejecutar server:
3)Migraciones a bd:
    En el directorio recetasapi (donde se encuentra el archivo manage.py)
    1. python manage.py makemigrations recetas
    2. python manage.py migrate recetas

4) Ejecutar server:
    En el directorio recetasapi (donde se encuentra el archivo manage.py)
    python manage.py runserver

Informaciones varias
    -El server se ejecuta por defecto en el puro 8000. En caso de querer cambiar puerto: python manage.py runserver <puerto>. (e.g. python manage.py runserver 8001)
    APIS:
        - /api/recetas/ : Permite GET. Obtiene el listado de recetas. Regresa {"id" : "<id>", "titulo" : "<titulo de la receta>", "imagen" : "<direccion de la imagen>" }
        - /api/receta/nueva/ : Permite POST. Los campos del json deben ser:
            "titulo" : máximo 80 caracteres.
            "imagen": máximo 120 caracteres. Por defecto se usa: "https://i.blogs.es/87930e/comidas-ricas/1366_2000.jpg" (si está vacío)
            "ingredientes": Listado de ingredientes/strings.
            "preparacion": Listado de pasos/strings.
        - api/recetas/<int:pk>/ : Permite GET, PUT y DELETE. Los campos obtenidos del json (y necesarios para update/put) son todos (id, titulo, imagen, ingredientes[], preparacion[]). 
            *Reemplazar <int:pk> con la id de la receta a ver (y actualizar o borrar). ID obtenida desde api/recetas/....
    Otro:
        - En caso de querer probar las apis en el navegador directamente. abrir localhost:<puerto>/api/...
            - Para agregar una receta usando la /api/recetas/,ir al archivo /recetas/views.py y seguir instrucciones comentadas ahí.