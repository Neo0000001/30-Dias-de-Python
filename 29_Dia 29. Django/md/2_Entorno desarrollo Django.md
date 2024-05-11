### Puesta en marcha de un entorno de desarrollo Django

Ahora que sabes para qué se utiliza Django, te enseñaremos cómo configurar y probar un entorno de desarrollo Django en Windows, 
Linux (Ubuntu), y Mac OS X — cualquiera que sea el sistema operativo común que estés utilizando, este artículo te dará lo que 
necesitas para ser capaz de empezar a desarrollar aplicaciones Django.

# Visión general del entorno de desarrollo Django

Django hace muy fácil configurar tu computadora de manera que puedas empezar a desarrollar aplicaciones web. Esta sección explica 
qué consigues con el entorno de desarrollo y proporciona una visión general de algunas de tus opciones de puesta en marcha y 
configuración. El resto del artículo explica el método recomendado de instalación del entorno de desarrollo de Django en Ubuntu, 
Mac OS X, y Windows, y cómo puedes probarlo.

# ¿Qué es el entorno de desarrollo Django?

El entorno de desarrollo es una instalación de Django en tu computadora local que puedes usar para desarrollar y probar apps Django 
antes de desplegarlas al entorno de producción.

Las principales herramientas que el mismo Django proporciona son un conjunto de scripts de Python para crear y trabajar con proyectos 
Django, junto con un simple servidor web de desarrollo que puedes usar para probar de forma local (es decir en tu computadora, no en 
un servidor web externo) aplicaciones web Django con el explorador web de tu computadora.

Hay otras herramientas periféricas, que forman parte del entorno de desarrollo, que no cubriremos aquí. Estas incluyen cosas como un 
editor de textos (en-US) o IDE para editar código, una herramienta de gestión del control de fuentes como Git para gestionar con seguridad las diferentes versiones de tu código. Asumimos que tienes ya un editor de textos instalado.

# ¿Cuáles son las opciones de puesta en marcha de Django?

Django es extremadamente flexible en términos de cómo y dónde puede instalarse y configurarse. Django puede ser:

1. Instalado en diferentes sistemas operativos.
2. Ser usado con Python 3 y Python 2.
3. instalado desde las fuentes, desde el Python Package Index (PyPi) y en muchos casos desde la aplicación de gestión de paquetes de la computadora.
4. Configurado para usar una de entre varias bases de datos, que pueden también necesitar ser instaladas y configuradas por separado.
5. Ejecutarse en el entorno Python del sistema principal o dentro de entornos virtuales Python separados.

Cada una de estas opciones requieren configuraciones y puesta en marcha ligeramente diferentes. Las siguientes subsecciones explican 
algunas de tus opciones. En el resto del artículo te mostraremos como ajustar Django en un pequeño número de sistemas operativos, 
y se supondrá ese ajuste a lo largo del resto del módulo.

# ¿Qué sistemas operativos están soportados?

Las aplicaciones web Django pueden ejecutarse en casi cualquier máquina donde pueda funcionar el lenguaje de programación 
Python: Windows, Mac OS X, Linux/Unix, Solaris, por nombrar sólo unos pocos. Casi cualquier computadora debería tener el 
rendimiento necesario para ejecutar Django durante el desarrollo.

En este artículo proporcionamos instrucciones para Windows, Mac OS X, y Linux/Unix.

# ¿Qué versión de Python deberías usar?

Django se ejecuta por encima de Python, y puede uarse tanto con Python 2 o con Python 3 (o ambos). Cuando estés seleccionando una versión deberías tener en cuenta que:

Python 2 es una versión tradicional del lenguaje que no va a tener más características nuevas pero que tiene disponible para los 
desarrolladores, un enorme repositorio de bibliotecas de terceros de alta calidad (algunas de las cuales no están disponibles en Python 3). Python 3 es una actualización de Python 2 que, aunque similar, es más consistente y fácil de usar. Python 3 también es el futuro de Python, y continúa su evolución.

También es posible soportar ambas versiones usando bibliotecas (ej. six), aunque no sin un esfuerzo adicional de desarrollo.

Nota: 

Historicamente Python 2 era la única elección realista, porque muy pocas bibliotecas de terceros estaban disponibles para Python 3. 
La tendencia actual es que la mayoría de paquetes nuevos y populares del Python Package Index (PyPi) soporten ambas versiones de Python. 
Aunque todavía haya muchos paquetes que sólo están disponibles para Python 2, elegir Python 3 es actualmente una opción muy popular.

Te recomendamos que uses la última versión de Python 3 a menos que el sitio dependa de bibliotecas de terceros que sólo están disponibles para Python 2.

Este artículo te explicará como instalar un entorno para Python 3 (el ajuste equivalente para Python 2 sería muy similar).

# ¿Dónde puedo descagarme Django?

Hay tres lugares para descargar Django:

El Python Package Repository (PyPi), usando la herramienta pip. Este es el mejor modo de obtener la última veersión estable de Django.
Usar una versión del gestor de paquetes de tu computadora. Las distribuciones de Django que se empaquetan con los sistemas operativos 
ofrecen un mecanismo de instalación ya familiar. Ten en cuenta sin embargo que la versión empaquetada puede ser bastante antigua, y sólo puede ser instalada en el entorno de Python del sistema (que puede no ser el que tu quieras).
Instalar desde la fuente. Puedes obtener y descargar la versión con el último grito de Python partiendo de las fuentes. Esto no es lo 
recomendable para principiantes, pero es necesario cuando estás listo para empezar a contribuir codificando el propio Django.
Este artículo te muestra como instalar Django desde PyPi, para conseguir la última versión estable.

# ¿Qué base de datos?

Django soporta cuatro bases de datos importantes (PostgreSQL, MySQL, Oracle y SQLite), y hay bibliotecas comunitarias que proporcionan varios niveles de soporte para otras bases de datos populares SQL y NOSQL. Te recomendamos que elijas la misma base de datos tanto para la producción como para el desarrollo (aunque Django abstrae muchas de las diferencias entre las bases usando su Object-Relational Mapper (ORM), hay todavía problemas potenciales que es mejor evitar).

Durante este artículo (y la mayoría de este módulo) usaremos la base de datos SQLite, que almacena sus datos en un fichero. SQLite está pensado para ser usado como base ligera y no puede soportar un alto nivel de concurrencia. Es sin embargo una excelente elección para aplicaciones que son principalmente de sólo lectura.

Nota:

Django está configurado para usar SQLite por defecto cuando comienzas tu proyecto de sitio web usando las herramientas estándard 
(django-admin). Es una gran elección cuando estás empezando porque no requiere configuración o puesta en marcha adicional.

# ¿Instalar Python en un entorno de sistema o virtual?

Cuando instalas Python3 obtienes un único entorno global que es compartido con todo el código Python3. Si bien puedes instalar los paquetes que te gusten en el entorno, sólo puedes instalar al mismo tiempo una versión en particular de cada paquete.

Nota: Las aplicaciones Python instaladas en el entorno global pueden entrar en conflicto potencialmente unas con otras (ej. si dependen de diferentes versiones del mismo paquete).

Si instalas Django dentro del entorno por defecto/global sólo podrás apuntar a una sóla versión de Django en la computadora. Esto puede ser un problema si quieres crear nuevos sitios (usando la última versión de Django) pero manteniendo los sitios web que dependen de versiones más antiguas.

Como resultado, los desarrolladores experimentados de Python/Django normalmente ejecutan las aplicaciones Python dentro de entornos virtuales Python independientes. De esta forma se habilitan múltiples entornos Django diferentes en la misma computadora. !El mismo equipo de desarrollo Django recomienda que uses entornos Python virtuales!

Este módulo da por supuesto que has instalado Django en un entorno virtual, y te mostraremos cómo hacerlo más abajo.

# Uso de Django dentro de un entorno virtual de Python

Las bibliotecas que usaremos para crear nuestros entornos virtuales están en virtualenvwrapper (Linux and Mac OS X) y virtualenvwrapper-win (Windows), que utilizan a su vez la herramienta virtualenv (en-US). Las herramientas wrapper crean una interfaz consistente para la gestión de interfaces en todas las plataformas.

# Instalación del software del entorno virtual

Puesta en marcha del entorno virtual en Ubuntu.

Después de instalar Python y pip puedes instalar virtualenvwrapper (que incluye virtualenv) usando pip3 como se muestra.

```bash
sudo pip3 install virtualenvwrapper
```

A continuación añade las siguientes líneas al final del fichero de inicio de tu shell (éste es un fichero oculto llamado .bashrc 
que se encuentra en tu directorio de inicio del usuario). Ésto ajusta la localización de donde deberían vivir los entornos virtuales, 
la localización de los directorios de tus proyectos de desarrollo, y la localización del script instalado con este paquete:

```bash
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

A continuación volver a recargar el fichero de inicio ejecutando el siguiente comando en el terminal:

```bash
source ~/.bashrc
```

En este punto deberías ver un puñado de scripts empezando a ejecutarse como se muestra a continuación:

```bash
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/premkproject
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/postmkproject
...
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/preactivate
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/postactivate
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/get_env_details
```

Ahora puedes crear un nuevo entorno virtual con el comando mkvirtualenv.

# Uso de un entorno virtual

Hay sólo otros pocos comandos útiles que deberías conocer, hay más en la documentación de la herramienta, pero éstos son los que usarás de forma habitual:

```bash
deactivate — Salir del entorno virutal Python actual
workon — Listar los entornos virtuales disponibles
workon name_of_environment — Activar el entorno virtual Python especificado
rmvirtualenv name_of_environment — Borrar el entorno especificado.
```

# Instalación de Django

Una vez que has creado el entorno virtual, y realizado la llamada workon para entrar en él, puedes usar pip3 para instalar Django.

```bash
pip3 install django
```

Puedes comprobar que está instalado Django ejecutando el siguiente comando (esto sólo comprueba que Python puede encontrar el módulo Django):

# Linux/Mac OS X

```bash
python3 -m django --version
 1.11.7
```

# Windows

```bash
py -3 -m django --version
 1.11.7
```

# Comprobación de tu instalación

La prueba de arriba funciona, pero no es muy divertida. Una comprobación más interesante es crear un esqueleto de proyecto y ver si 
funciona. Para hacer ésto, navega primero en tu consola de comandos/terminal a donde quieras almacenar tus aplicaciones Django. 
Crea una carpeta para la comprobación de tu sitio y navega a ella.

```bash
mkdir django_test
cd django_test
Copy to Clipboard
```

Puedes crear a continuación un nuevo esqueleto de sitio llamado "mytestsite" usando la herramienta django-admin como se muestra a 
continuación. Después de crear el sitio puedes navegar a la carpeta donde encontrarás el script principal para la gestión de proyectos, llamado manage.py.

```bash
django-admin startproject mytestsite
cd mytestsite
Copy to Clipboard
```

Podemos arrancar el servidor web de desarrollo desde esta carpeta usando manage.py y el comando runserver, como se muestra.

```bash
$ python3 manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, 
contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

September 19, 2016 - 23:31:14
Django version 1.10.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Copy to Clipboard
```

Nota: El comando anterior muestra el comando Linux/Mac OS X. En este punto ¡puedes ignorar las advertencias sobre "13 unapplied migration(s)"!

Una vez que tengas funcionando el servidor puedes ver el sitio navegando a la siguiente URL en tu explorador web local: 
http://127.0.0.1:8000/. Deberías ver un sitio parecido a este:

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment/django_skeleton_app_homepage_django_4_0.png

