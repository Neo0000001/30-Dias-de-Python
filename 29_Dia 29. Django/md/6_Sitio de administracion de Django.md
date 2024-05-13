### Tutorial Django Parte 4: Sitio de Administración de Django

Ahora que hemos creado modelos para el sitio web de la BibliotecaLocal, usaremos el sitio de administración de Django para añadir 
algunos datos de libros "reales". Primero mostraremos cómo registrar los modelos en el sitio de administración y luego te mostraremos 
cómo iniciar sesión y crear algunos datos. Al final del artículo mostraremos algunas formas en las que puedes mejorar más adelante la 
presentación del sitio de Administración.

# Introducción

La aplicación de administración de Django puede usar tus modelos para construir automáticamente un área dentro del sitio que puedes 
usar para crear, consultar, actualizar y borrar registros. Esto puede ahorrarte mucho tiempo de desarrollo, haciendo muy fácil probar 
tus modelos y darte una idea de si tus datos son correctos. La aplicación de administración también puede ser útil para manejar datos 
en producción, dependiendo del estilo del sitio web. Desde el proyecto Django solo se recomienda para gestión de datos internos (por 
ejemplo, solo para uso de administradores o personas internas de tu organización), ya que como enfoque centrado en el modelo no es 
necesariamente la mejor interfaz posible para todos los usuarios, exponiendo una gran cantidad de detalles innecesarios de los 
modelos.

Toda la configuración requerida para incluir la aplicación admin en tu sitio Web fue hecha automaticamente cuando creaste el 
esqueleto del proyecto (para información sobre dependencias reales necesarias, vea los documentos de Django aquí). Como resultado, 
todo lo que debes hacer para agregar tus modelos a la aplicación admin es registrarlos. Al final de este artículo entregaremos una 
breve demostración sobre como puedes configurar aún más el área de administración para mejorar la visualización de nuestros modelos
de datos.

Después de registrar los modelos te mostraremos como crear un nuevo "administrador", iniciar sesión en el sitio, y crear algunos 
libros, autores, instancias de libros, y géneros. Esto será útil para probar las vistas y plantillas que empezaremos a crear en el 
siguiente tutorial.

# Registrando los modelos

Primero, abre admin.py en la aplicación catálogo (/locallibrary/catalog/admin.py). Actualmente se ve como esto — notar que ya importa 
django.contrib.admin:

```python
from django.contrib import admin

# Register your models here.
```

Registra los modelos copiando el texto siguiente al final del archivo. Este simple código esta importando los modelos y después llama 
a admin.site.register para registrar a cada uno de ellos.

```python
from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
```

Nota: Si tu aceptaste el desafío de crear un modelo que represente el Lenguaje natural de un libro (ver el artículo tutorial de 
modelos), importalo y registralo también!

Esta es la forma más simple de registrar un modelo, o modelos, con el sitio. El sitio de administración es altamente personalizable, 
y hablaremos más sobre otras formas de registrar tus modelos más abajo.

# Creando un administrador

Para iniciar sesión en el sitio de administración, necesitamos una cuenta de usuario con estado de Personal habilitado. Para ver y 
crear registros tambien necesitamos que este usuario tenga permisos para administrar todos nuestros objetos. Puedes crear una cuenta 
"administrador" que tenga acceso total al sitio y a todos los permisios necesarios usando manage.py.

Usa el siguiente comando, en el mismo directorio de manage.py, para crear al administrador. Deberás ingresar un nombre de usuario, 
dirección email, y una contraseña fuerte.

```bash
python3 manage.py createsuperuser
```

Una vez el comando termine un nuevo administrador será agregado a la base de datos. Ahora reinicia el servidor de desarrollo para que 
podamos probrar el inicio de sesión:

```bash
python3 manage.py runserver
```

# Iniciar sesión y usar el sitio

Para iniciar sesión en el sitio, ve a la URL /admin (e.j. http://127.0.0.1:8000/admin) e ingresa tus credenciales de id usuario y 
contraseña de administrador (serás redirigido a la página login, y entonces volverás a la URL de /admin después de haber ingresado 
tus datos).

Esta parte del sitio muestra todos tus modelos, agrupados por aplicación instalada. Puedes hacer click en un nombre de modelo para ir 
a una pantalla que lista todos los registros asociados, y además puedes hacer click sobre esos registros para editarlos. También 
puedes hacer click directamente sobre el vínculo Añadir a continuación de cada modelo para comenzar a crear un registro de ese tipo.

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site/admin_home.png

Haz click sobre el vínculo Añadir a la derecha de Books para crear un nuevo libro, esto mostrará un diálogo parecido al de abajo. 
Nota como los títulos de cada campo, el tipo de widget usado, y el help_text (si existe) corresponde con el valor que especificaste 
en el modelo.

Ingresa valores para los campos. Puede crear nuevos autores o géneros presionandoel botón + a continuación del campo respectivo (o 
seleccionar un valor existente de las listas si ya las tenías creadas). Cuando termines puedes presionar Grabar, Grabar y añadir 
otro, o Grabar y continuar editando para guardar el registro.

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site/admin_book_add.png

Nota: En este punto nos gustaría que pasaras algún tiempo añadiendo unos pocos libros, autores, y géneros (ej. Fantasía) a tu 
aplicación. Asegúrate de que cada autor y género incluye un par de libros diferentes (esto hará tus vistas de lista y detalle más 
interesantes cuando las implementemos más tarde en la serie de artículos).

Cuando hayas terminado de añadir libros, haz click en el enlace Home en el separador de arriba para regresar a la página principal de 
administración. Luego haz click en el enlace Books para desplegar la lista actual de libros (o en alguno de los otros enlaces para 
ver las listas de otros modelos). Ahora que haz añadido unos cuantos libros, la lista debería lucir similar a la captura de pantalla 
de abajo. Se muestra el título de cada libro; que es el valor devuelto por el método __str__() del modelo Book que especificamos en 
el artículo anterior.

https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Admin_site/admin_book_list.png

Desde esta lista puedes eliminar libros marcando la casilla de verificación junto al libro que no deseas y seleccionando la acción 
delete... en la lista de selección Action, y luego presionando el botón Go. Puedes también añadir nuevos libros presionando el botón 
ADD BOOK.

Puedes editar un libro haciendo click en su nombre en la lista. La página de edición para un libro, como se muestra abajo, es casi 
idéntica a la página "Add". Las principales diferencias son el título de la página (Change book) y la adición de los botones Delete, 
HISTORY y VIEW ON SITE (este último aparece porque definimos el método get_absolute_url() en nuestro modelo).

https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Admin_site/admin_book_modify.png

Ahora regresa a la página Home (usando el enlace Home de la barra superior) y observa las listas Author y Genre -- ya deberías tener 
algunos registros creados de cuando añadiste los nuevos libros, pero puedes crear algunos más.

Lo que no vas a tener es BookInstances, porque estas no se crean de los libros (si bien puedes crear un Book desde una BookInstance 
-- esta es la naturaleza de los campos ForeignKey). Regresa a la página Home y presiona el botón Add relacionado para desplegar la 
pantalla Add book instance, como se muestra abajo. Nota el largo y globalmente único Id, que puede ser usado para identificar 
inequívocamente una única copia de un libro dentro de la biblioteca.

https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Admin_site/admin_bookinstance_add.png

Crea algunos de estos registros para cada uno de tus libros. Establece el status en Available para al menos algunos registros y en On 
loan para otros. Si el status es diferente de Available, especifica también una fecha de Due back (devolución).

¡Eso es todo! Has aprendido a configurar y usar el sitio de administración. También has creado registros para Book, BookInstance, 
Genre y Author que podremos usar una vez que creemos nuestras propias views (vistas) y templates (plantillas).

# Configuración avanzada

Django hace un gran trabajo al crear un sitio de administración básico usando la información de los modelos registrados:

1. Cada modelo tiene una lista de registros individuales, identificados por la cadena creada por el método __str__() del modelo, y 
enlazados a vistas/formularios de detalle para edición. Por defecto, esta vista de lista tiene un menú de acción en la parte superior 
que puedes usar para realizar operaciones de eliminación masiva de los registros.

2. Los formularios de detalle de registro del modelo para edición y adición de registros contienen todos los campos del modelo, 
organizados verticalmente en su orden de declaración.

Posteriormente puedes personalizar la interfaz para hacerla incluso más fácil de usar. Algunas de las cosas que puedes hacer son:

Vistas de lista:

1. Añadir campos e información adicional desplegada para cada registro.
2. Añadir filtros para seleccionar qué registros se listan, basados en fechas u otros tipos de valores (ej. estado de préstamo del 
libro).
3. Añadir opciones adicionales al menú Action en las vistas de lista y elegir en qué lugar del formulario se despliega este menú.

Vistas de detalle:

1. Elegir qué campos desplegar (o excluir), junto con su orden, agrupamiento, si son editables, el tipo de control a usarse, 
orientación, etc.
2. Añadir campos relacionados a un registro para permitir la edición en cadena (ej. proveer la capacidad de añadir y editar registros 
de libros mientras estás creando su registro de autor).

En esta sección observaremos unos cuantos cambios que mejorarán la interfaz de nuestra LocalLibrary, incluyendo la adición de más 
información a las listas de los modelos Book y Author, y mejorando el diseño de sus vistas de edición. No cambiaremos la presentación 
de los modelos Language y Genre debido a que solo tienen un campo cada uno, ¡por lo que no hay ningún beneficio real de hacerlo!

Puedes encontrar una referencia completa de todas las opciones de personalización del sitio de administración en The Django Admin
site (Django Docs).

https://docs.djangoproject.com/en/1.10/ref/contrib/admin/

# Registrar una clase ModelAdmin

Para cambiar la forma en la que un modelo se despliega en la interfaz de administración debes definir una clase ModelAdmin (que 
describe el diseño) y registrarla con el modelo.

Comencemos con el modelo Author. Abre admin.py en la aplicación catalog (/locallibrary/catalog/admin.py). Comenta tu registro 
original para el modelo Author (colocando el prefijo # en la línea):

```python
# admin.site.register(Author)
```

Ahora añade una nueva clase AuthorAdmin y regístrala como se muestra abajo.

```python
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
```

Ahora añadiremos clases ModelAdmin para Book, y BookInstance. De nuevo, debemos comentar nuestros registros originales:

```python
#admin.site.register(Book)
#admin.site.register(BookInstance)
```

Ahora, para crear y registar los nuevos modelos usaremos, para propósitos de esta demostración, la expresión @register para registrar los modelos (hace exactamente lo mismo que admin.site.register()):

```python
# Register the Admin classes for Book using the decorator

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
```

Al momento todas nuestras clases de administración estás vacías (observa "pass"), así que el comportamiento de administración ¡no 
cambiará! Ahora podemos extenderlas para definir nuestro comportamiento de administración específico para cada modelo.

# Configurar las vistas de lista

La LocalLibrary actualmente lista todos los autores usando el nombre generado por el método __str__() del modelo. Esto funciona bien 
cuando solo tienes unos pocos autores, pero una vez que tienes muchos puedes terminar teniendo duplicados. Para diferenciarlos, o 
simplemente para mostrar información más interesante sobre cada autor, puedes usar list_display para añadir otros campos a la vista.

Reemplaza tu clase AuthorAdmin con el código de abajo. Los nombres de campos a ser desplegados en la lista están declarados en una 
tupla en el orden requerido, como se muestra (estos son los mismos nombres especificados en tu modelo original).

```python
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
```

Recarga el sitio y navega hacia la lista de autores. Ahora deberían desplegarse los campos de arriba, así:

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site/admin_improved_author_list.png

Para nuestro modelo Book desplegaremos adicionalmente el author y genre. El author es un campo de relación tipo ForeignKey (uno a 
uno), y por tanto estará representado por el valor __str__() del registro asociado. Reemplaza la clase BookAdmin con la versión de 
abajo.

```python
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
```

Desafortunadamente, no podemos especificar directamente el campo genre en list_display porque es un campo ManyToManyField (Django 
previene esto porque habría un alto "costo" de acceso a base de datos si lo hiciera). En lugar de eso, definiremos una función 
display_genre para obtener la información como una cadena (esta es la función que hemos llamado arriba; la definiremos más abajo).

Nota: Obtener el genre podría no ser una buena idea aquí, debido al "costo" de la operación en la base de datos. Te mostramos cómo 
hacerlo porque llamar funciones desde tus modelos puede ser muy útil por otras razones -- por ejemplo para añadir un enlace Delete 
junto a cada ítem en la lista.

Añade el siguiente código en tu modelo Book (models.py). Esto crea una cadena con los tres primeros valores del campo genre (si 
existen) y crea una short_description (descripción corta) que puede ser usada en el sitio de administración por este método.

```python
def display_genre(self):
    """
    Creates a string for the Genre. This is required to display genre in Admin.
    """
    return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
display_genre.short_description = 'Genre'
```

Después de guardar el modelo y actualizar admin, recarga el sitio y ve a la página de lista de Books (libros), deberías ver una lista 
de libros como la de abajo:

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site/admin_improved_book_list.png

El modelo Genre (y el modelo Language, si lo definiste) tiene un solo campo, por lo que no tiene sentido crear un modelo adicional 
para el mismo para desplegar campos adicionales.

Nota: Vale la pena actualizar el modelo BookInstance para mostrar al menos el estado y fecha de devolución esperada. ¡Lo hemos 
añadido como un reto al final de este artículo!

# Añadir filtros de lista