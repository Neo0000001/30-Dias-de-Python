### 30 Dias de Python: Dia 27 - Selenium

# Resumen rápido de Selenium 4

Selenium 4 es la última versión importante del marco de pruebas de automatización Selenium. Fue lanzado en octubre de 2021 e incluye 
una serie de nuevas características y mejoras.

1. Algunas de las principales características nuevas de Selenium 4 incluyen:

2. Ciclo de vida de WebDriver: Selenium 4 introduce un nuevo ciclo de vida de WebDriver, lo que facilita la administración de la 
   duración de los objetos WebDriver.

3. Localizadores relativos: Selenium 4 introduce localizadores relativos, lo que facilita la ubicación de elementos en una página web.

4. Interceptación de red: Selenium 4 incluye compatibilidad con la interceptación de red, lo que le permite interceptar y modificar 
   el tráfico de la red.

5. ID de elemento de WebDriver: Selenium 4 introduce los ID de elemento de WebDriver, que son identificadores únicos para los 
   elementos en una página web.

6. WebDriver W3C: Selenium 4 ahora es totalmente compatible con el estándar W3C WebDriver.

Además de estas nuevas características, Selenium 4 también incluye una serie de otras mejoras, como:

- Rendimiento mejorado: Selenium 4 es significativamente más rápido que las versiones anteriores de Selenium.
- Manejo de errores mejorado: Selenium 4 incluye un manejo de errores mejorado, lo que facilita la depuración de scripts de prueba.
- Nueva documentación: Selenium 4 incluye un nuevo conjunto de documentación más completo.

En general, Selenium 4 es una mejora significativa con respecto a las versiones anteriores de Selenium. Incluye una serie de nuevas 
características y mejoras que facilitan la automatización de las pruebas de navegadores web.

Aquí hay algunos de los beneficios de usar Selenium 4:

1. Es una herramienta multiplataforma: Selenium 4 se puede usar en Windows, macOS y Linux.
2. Es de código abierto: Selenium 4 es un proyecto de código abierto, lo que significa que es gratuito de usar y modificar.
3. Es compatible con una gran comunidad: Hay una gran comunidad de usuarios y desarrolladores de Selenium que pueden ayudarlo a 
   solucionar problemas y aprender a usar la herramienta.
4. Es fácil de aprender: Selenium 4 es relativamente fácil de aprender, incluso para los principiantes.
5. Si está buscando una herramienta poderosa y versátil para automatizar las pruebas de navegadores web, entonces Selenium 4 es una 
   excelente opción.

# WebDriver

WebDriver maneja un navegador de forma nativa, como lo haría un usuario, ya sea localmente o en una máquina remota usando el servidor 
Selenium, marca un salto adelante en términos de automatización del navegador.

Selenium WebDriver se refiere tanto a los enlaces de lenguaje como a las implementaciones del código de control del navegador 
individual. Esto se conoce comúnmente como simplemente WebDriver.

Selenium WebDriver es una recomendación W3C

WebDriver está diseñado como una interfaz de programación simple y más concisa.

WebDriver es una API compacta orientada a objetos.

## Conduce el navegador de manera efectiva.

# Empezando

Si es nuevo en Selenium, tenemos algunos recursos que pueden ayudarlo a ponerse al día de inmediato.
Selenium admite la automatización de todos los principales navegadores del mercado mediante el uso de WebDriver. WebDriver es una 
API y un protocolo que define una interfaz independiente del lenguaje para controlar el comportamiento de los navegadores web. Cada 
navegador está respaldado por una implementación específica de WebDriver, llamada controlador. El controlador es el componente 
responsable de delegar en el navegador y maneja la comunicación hacia y desde Selenium y el navegador.

Esta separación es parte de un esfuerzo consciente para que los proveedores de navegadores asuman la responsabilidad de la 
implementación de sus navegadores. Selenium hace uso de estos controladores de terceros cuando es posible, pero también proporciona 
sus propios controladores mantenidos por el proyecto para los casos en que esto no sea una realidad.

El marco de Selenium une todas estas piezas a través de una interfaz orientada al usuario que permite que los diferentes backends del 
navegador se utilicen de forma transparente, lo que permite la automatización entre navegadores y plataformas.

La configuración de Selenium es bastante diferente de la configuración de otras herramientas comerciales. Antes de que pueda comenzar 
a escribir el código de Selenium, debe instalar las bibliotecas de enlaces de lenguaje para su lenguaje de elección, el navegador que 
desea usar y el controlador para ese navegador.

# Funcionalidad específica de Chrome

Estas son capacidades y características específicas de los navegadores Google Chrome.
De forma predeterminada, Selenium 4 es compatible con Chrome v75 y superior. Tenga en cuenta que la versión del navegador Chrome y la 
versión de chromedriver deben coincidir con la versión principal.

# Opciones

Las capacidades comunes a todos los navegadores se describen en la página Opciones.

Las capacidades exclusivas de Chrome y Chromium están documentadas en la página de Google para capacidades y opciones de Chrome.

Comenzar una sesión de Chrome con opciones definidas básicas se ve así:

```python
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
```

Ver ejemplo completo en GitHub:

https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/browsers/test_chrome.py#L10-L11

# Argumentos

El argsparámetro es para una lista de modificadores de línea de comandos que se utilizarán al iniciar el navegador. Hay dos recursos 
excelentes para investigar estos argumentos:

Banderas cromadas para herramientas
Lista de modificadores de línea de comandos de Chromium
Los argumentos comúnmente utilizados incluyen --start-maximized, --headless=newy--user-data-dir=...

Agregue un argumento a las opciones:

```python
    options.add_argument("--start-maximized")
```

Ver ejemplo completo en GitHub:

https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/browsers/test_chrome.py#L18

# Inicie el navegador en una ubicación específica

El binaryparámetro toma la ruta de una ubicación alternativa del navegador para usar. Con este parámetro, puede usar chromedriver 
para controlar varios navegadores basados en Chromium.

Agregue una ubicación del navegador a las opciones:

```python
driver_path = '/home/enrique/ChromeDriver/chromedriver'
```

# Agregar extensiones

El extensionsparámetro acepta archivos crx. En cuanto a los directorios desempaquetados, utilice el load-extensionargumento en su 
lugar, como se menciona en esta publicación.

Agregue una extensión a las opciones:

```python
chrome_options.add_extension(path)
```

Ver ejemplo completo en GitHub:

https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/browsers/test_chrome.py#L105

# Mantener el navegador abierto

Establecer el detachparámetro en verdadero mantendrá el navegador abierto después de que finalice el proceso, siempre que no se envíe 
el comando de salida al controlador.

Agregue un binario a las opciones:

```python
options.add_experimental_option("detach", True)
```

Ver ejemplo completo en GitHub:

https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/browsers/test_chrome.py#L28

# Excluyendo argumentos

Chromedriver tiene varios argumentos predeterminados que utiliza para iniciar el navegador. Si no desea que se agreguen esos 
argumentos, páselos a excludeSwitches. Un ejemplo común es volver a activar el bloqueador de ventanas emergentes. Se puede analizar 
una lista completa de argumentos predeterminados desde el código fuente de Chromium.

# Establecer argumentos excluidos en las opciones:

```python
options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
```

Ver ejemplo completo en GitHub:

https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/browsers/test_chrome.py#L38

# Servicio

Se pueden encontrar ejemplos para crear un objeto de servicio predeterminado y para configurar la ubicación y el puerto del 
controlador en la página Servicio del controlador.

# Salida de registro

Obtener registros de controladores puede ser útil para problemas de depuración. La clase Servicio le permite dirigir dónde irán los 
registros. La salida de registro se ignora a menos que el usuario la dirija a alguna parte.

# Salida de archivo

Para cambiar la salida de registro para guardar en un archivo específico:

```python
service = webdriver.chrome.service.Service(log_path=log_path)
```

Ver ejemplo completo en GitHub:

https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/browsers/test_chrome.py#L47

# Nivel de registro

Hay 6 niveles de registro disponibles: ALL, DEBUG, INFO, WARNING, SEVEREy OFF. Tenga en cuenta que --verbosees equivalente a 
--log-level=ALLy --silentes equivalente a --log-level=OFF, por lo que este ejemplo solo establece el nivel de registro de forma 
genérica:

```python
service = webdriver.chrome.service.Service(service_args=['--log-level=DEBUG'], log_path=log_path)
```

Ver ejemplo completo en GitHub:

https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/browsers/test_chrome.py#L70

# Características del archivo de registro

Hay 2 funciones que solo están disponibles al iniciar sesión en un archivo:

1. Agregar registro
2. Marcas de tiempo legibles

Para usarlos, también debe especificar explícitamente la ruta de registro y el nivel de registro. La salida del registro será 
administrada por el controlador, no por el proceso, por lo que es posible que se observen diferencias menores.

```python
service = webdriver.chrome.service.Service(service_args=['--append-log', '--readable-timestamp'], log_path=log_path)
```

Ver ejemplo completo en GitHub:

https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/browsers/test_chrome.py#L81

# Deshabilitar verificación de compilación

Las versiones del navegador Chromedriver y Chrome deben coincidir y, de no ser así, el controlador generará un error. Si deshabilita 
la verificación de compilación, puede forzar el uso del controlador con cualquier versión de Chrome. Tenga en cuenta que esta es una 
función no admitida y los errores no se investigarán.

```python
service = webdriver.chrome.service.Service(service_args=['--disable-build-check'], log_path=log_path)
```

Ver ejemplo completo en GitHub:

https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/browsers/test_chrome.py#L92

# Características especiales

Algunos navegadores han implementado características adicionales que son únicas para ellos.

# Estrategias de espera

Quizás el desafío más común para la automatización del navegador es garantizar que la aplicación web esté en condiciones de ejecutar 
un comando particular de Selenium según se desee. Los procesos a menudo terminan en una condición de carrera en la que, a veces, el 
navegador entra primero en el estado correcto (las cosas funcionan según lo previsto) y, a veces, el código de Selenium se ejecuta 
primero (las cosas no funcionan según lo previsto). Esta es una de las principales causas de las pruebas escamosas.

Todos los comandos de navegación esperan un readyStatevalor específico basado en la estrategia de carga de la página (el valor 
predeterminado para esperar es "complete") antes de que el controlador devuelva el control al código. El readyStateúnico problema es 
cargar recursos definidos en el HTML, pero los recursos de JavaScript cargados a menudo generan cambios en el sitio, y es posible que 
los elementos con los que es necesario interactuar aún no estén en la página cuando el código esté listo para ejecutar el siguiente 
comando de Selenium.

De manera similar, en muchas aplicaciones de una sola página, los elementos se agregan dinámicamente a una página o cambian de 
visibilidad en función de un clic. Un elemento debe estar presente y mostrarse en la página para que Selenium interactúe con él.

Tome esta página, por ejemplo: https://www.selenium.dev/selenium/web/dynamic.html Cuando el mensaje "¡Agregar un cuadro!" se hace 
clic en el botón, se crea un elemento "div" que no existe. Cuando se hace clic en el botón "Revelar una nueva entrada", se muestra un 
elemento de campo de texto oculto. En ambos casos la transición toma un par de segundos. Si el código de Selenium debe hacer clic en 
uno de estos botones e interactuar con el elemento resultante, lo hará antes de que ese elemento esté listo y falle.

La primera solución a la que muchas personas recurren es agregar una declaración de suspensión para pausar la ejecución del código 
durante un período de tiempo determinado. Debido a que el código no puede saber exactamente cuánto tiempo debe esperar, esto puede 
fallar cuando no duerme lo suficiente. Alternativamente, si el valor se establece demasiado alto y se agrega una declaración de
suspensión en cada lugar que se necesita, la duración de la sesión puede volverse prohibitiva.

Selenium proporciona dos mecanismos diferentes para la sincronización que son mejores.

# Esperas implícitas

Selenium tiene una forma integrada de esperar automáticamente los elementos llamada espera implícita. Se puede establecer un valor 
de espera implícito con la capacidad de tiempos de espera en las opciones del navegador o con un método de controlador (como se 
muestra a continuación).

Esta es una configuración global que se aplica a cada llamada de ubicación de elemento para toda la sesión. El valor predeterminado 
es 0, lo que significa que si no se encuentra el elemento, devolverá inmediatamente un error. Si se establece una espera implícita, 
el controlador esperará la duración del valor proporcionado antes de devolver el error. Tenga en cuenta que tan pronto como se 
localice el elemento, el controlador devolverá la referencia del elemento y el código seguirá ejecutándose, por lo que un valor de 
espera implícito mayor no aumentará necesariamente la duración de la sesión.

Advertencia: no mezcle esperas implícitas y explícitas. Si lo hace, puede causar tiempos de espera impredecibles. Por ejemplo, 
establecer una espera implícita de 10 segundos y una espera explícita de 15 segundos podría causar un tiempo de espera después de 20 
segundos.

Resolver nuestro ejemplo con una espera implícita se ve así:

```python
driver.implicitly_wait(2)
driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
driver.find_element(By.ID, "adder").click()

added = driver.find_element(By.ID, "box0")
```

Ver ejemplo completo en GitHub:

https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/waits/test_waits.py#L27-L31

# Esperas explícitas

Las esperas explícitas son bucles agregados al código que sondean la aplicación en busca de una condición específica para evaluarla 
como verdadera antes de que salga del bucle y continúe con el siguiente comando en el código. Si la condición no se cumple antes de 
un valor de tiempo de espera designado, el código generará un error de tiempo de espera. Dado que hay muchas formas de que la 
aplicación no esté en el estado deseado, las esperas explícitas son una excelente opción para especificar la condición exacta a 
esperar en cada lugar que se necesita. Otra buena característica es que, de forma predeterminada, la clase Selenium Wait espera 
automáticamente a que exista el elemento designado.

Este ejemplo muestra la condición que se espera como lambda. 

Python también es compatible con las condiciones esperadas:

https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html

```python
revealed = driver.find_element(By.ID, "revealed")
wait = WebDriverWait(driver, timeout=2)

driver.find_element(By.ID, "reveal").click()
wait.until(lambda d : revealed.is_displayed())

revealed.send_keys("Displayed")
```

Ver ejemplo completo en GitHub:

https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/waits/test_waits.py#L38-L44

# Personalización

La clase Wait se puede instanciar con varios parámetros que cambiarán la forma en que se evalúan las condiciones.

Esto puede incluir:

1. Cambiar la frecuencia con la que se evalúa el código (intervalo de sondeo).
2. Especificar qué excepciones deben manejarse automáticamente.
3. Cambiar la duración total del tiempo de espera.
4. Personalización del mensaje de tiempo de espera.

Por ejemplo, si el error del elemento no interactuable se vuelve a intentar de forma predeterminada, entonces podemos agregar una 
acción en un método dentro del código que se está ejecutando (solo debemos asegurarnos de que el código regrese truecuando sea 
exitoso):

```python
revealed = driver.find_element(By.ID, "revealed")
errors = [NoSuchElementException, ElementNotInteractableException]
wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)

driver.find_element(By.ID, "reveal").click()
wait.until(lambda d : revealed.send_keys("Displayed") or True)
```

Ver ejemplo completo en GitHub:

https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/waits/test_waits.py#L50-L55

### Elementos web

Identificar y trabajar con objetos de elementos en el DOM.
La mayoría del código Selenium de la mayoría de las personas implica trabajar con elementos web.

# Subir archivo

El cuadro de diálogo de carga de archivos se puede manejar con Selenium, cuando el elemento de entrada es de tipo archivo. Puede 
encontrar un ejemplo de ello en esta página web: https://the-internet.herokuapp.com/upload . Necesitaremos tener un archivo 
disponible con nosotros, que debemos cargar. El código para cargar el archivo para diferentes lenguajes de programación será el 
siguiente:

```python
from selenium import webdriver
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/upload");
driver.find_element(By.ID,"file-upload").send_keys("selenium-snapshot.jpg")
driver.find_element(By.ID,"file-submit").submit()
if(driver.page_source.find("File Uploaded!")):
    print("file upload success")
else:
    print("file upload not successful")
driver.quit()
```
  
Entonces, el código de ejemplo anterior ayuda a comprender cómo podemos cargar un archivo usando Selenium.

### Estrategias de localización

Formas de identificar uno o más elementos específicos en el DOM.
Un localizador es una forma de identificar elementos en una página. Es el argumento pasado a los métodos del elemento Finding.

# Encontrar elementos web

Ubicar los elementos en función de los valores de ubicación proporcionados.

Uno de los aspectos más fundamentales del uso de Selenium es obtener referencias de elementos para trabajar. Selenium ofrece una 
serie de estrategias de localización integradas para identificar un elemento de forma única. Hay muchas formas de utilizar los 
localizadores en escenarios muy avanzados. A los efectos de esta documentación, consideremos este fragmento de HTML:

```html
<ol id="vegetables">
 <li class="potatoes">…
 <li class="onions">…
 <li class="tomatoes"><span>Tomato is a Vegetable</span>…
</ol>
<ul id="fruits">
  <li class="bananas">…
  <li class="apples">…
  <li class="tomatoes"><span>Tomato is a Fruit</span>…
</ul>
```

# Primer elemento coincidente

Muchos localizadores coincidirán con varios elementos de la página. El método de elemento de búsqueda singular devolverá una 
referencia al primer elemento encontrado dentro de un contexto dado.

# Evaluación de DOM completo

Cuando se llama al método de búsqueda de elemento en la instancia del controlador, devuelve una referencia al primer elemento en el 
DOM que coincide con el localizador proporcionado. Este valor se puede almacenar y utilizar para futuras acciones de elementos. En 
nuestro ejemplo HTML anterior, hay dos elementos que tienen un nombre de clase de "tomates", por lo que este método devolverá el 
elemento en la lista de "verduras".

```python
vegetable = driver.find_element(By.CLASS_NAME, "tomatoes")
```
  
# Evaluación de un subconjunto del DOM

En lugar de encontrar un localizador único en todo el DOM, suele ser útil limitar la búsqueda al ámbito de otro elemento localizado. 
En el ejemplo anterior, hay dos elementos con un nombre de clase de "tomates" y es un poco más difícil obtener la referencia para el 
segundo.

Una solución es ubicar un elemento con un atributo único que sea un ancestro del elemento deseado y no un ancestro del elemento no 
deseado, luego llame a find element en ese objeto:

```python
fruits = driver.find_element(By.ID, "fruits")
fruit = fruits.find_element(By.CLASS_NAME,"tomatoes")
```

# Localizador optimizado

Es posible que una búsqueda anidada no sea la estrategia de ubicación más efectiva, ya que requiere que se emitan dos comandos 
separados para el navegador.

Para mejorar ligeramente el rendimiento, podemos usar CSS o XPath para encontrar este elemento en un solo comando. Consulte las 
sugerencias de la estrategia del localizador en nuestra sección Prácticas de prueba recomendadas.

Para este ejemplo, usaremos un Selector de CSS:

```python
fruit = driver.find_element(By.CSS_SELECTOR,"#fruits .tomatoes")
``` 

# Todos los elementos coincidentes

Hay varios casos de uso para necesitar obtener referencias a todos los elementos que coincidan con un localizador, en lugar de solo 
el primero. Los métodos de búsqueda de elementos plurales devuelven una colección de referencias de elementos. Si no hay 
coincidencias, se devuelve una lista vacía. En este caso, las referencias a todos los elementos de la lista de frutas y verduras se 
devolverán en una colección.

```python
plants = driver.find_elements(By.TAG_NAME, "li")
```

# Obtener elemento

A menudo, obtiene una colección de elementos pero quiere trabajar con un elemento específico, lo que significa que necesita iterar 
sobre la colección e identificar el que desea.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

    # Navigate to Url
driver.get("https://www.example.com")

    # Get all the elements available with tag name 'p'
elements = driver.find_elements(By.TAG_NAME, 'p')

for e in elements:
    print(e.text)
```

# Buscar elementos desde el elemento

Se utiliza para encontrar la lista de WebElements secundarios coincidentes dentro del contexto del elemento principal. Para lograr 
esto, el WebElement principal está encadenado con 'findElements' para acceder a los elementos secundarios.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com")

    # Get element with tag name 'div'
element = driver.find_element(By.TAG_NAME, 'div')

    # Get all the elements available with tag name 'p'
elements = element.find_elements(By.TAG_NAME, 'p')
for e in elements:
    print(e.text)
```
  
# Obtener elemento activo

Se utiliza para rastrear (o) encontrar el elemento DOM que tiene el foco en el contexto de navegación actual.

```python
  from selenium import webdriver
  from selenium.webdriver.common.by import By

  driver = webdriver.Chrome()
  driver.get("https://www.google.com")
  driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("webElement")

    # Get attribute of current active element
  attr = driver.switch_to.active_element.get_attribute("title")
  print(attr)
```

Consulte nuestras prácticas de prueba recomendadas para obtener consejos sobre localizadores , incluido cuál usar, cuándo y por qué 
declarar los localizadores por separado de los métodos de búsqueda.

# Localizadores tradicionales

Selenium brinda soporte para estas 8 estrategias de ubicación tradicionales en WebDriver:

```
Localizador                             Descripción

class name          Localiza elementos cuyo nombre de clase contiene el valor de búsqueda (no se permiten nombres de clase compuestos)
css selector        Localiza elementos que coinciden con un selector CSS
id                  Localiza elementos cuyo atributo ID coincide con el valor de búsqueda
name                Localiza elementos cuyo atributo NOMBRE coincide con el valor de búsqueda
link text           Localiza elementos de anclaje cuyo texto visible coincide con el valor de búsqueda
partial link text   Localiza elementos de anclaje cuyo texto visible contiene el valor de búsqueda. Si coinciden varios elementos, 
                    solo se seleccionará el primero.
tag name            Localiza elementos cuyo nombre de etiqueta coincide con el valor de búsqueda
xpath               Localiza elementos que coinciden con una expresión XPath
```

# Creación de localizadores

Para trabajar en un elemento web usando Selenium, primero debemos ubicarlo en la página web. Selenium nos proporciona las formas 
mencionadas anteriormente, mediante las cuales podemos ubicar el elemento en la página. Para comprender y crear un localizador, 
utilizaremos el siguiente fragmento de código HTML.

```html
<html>
<body>
<style>
.information {
  background-color: white;
  color: black;
  padding: 10px;
}
</style>
<h2>Contact Selenium</h2>

<form action="/action_page.php">
  <input type="radio" name="gender" value="m" />Male &nbsp;
  <input type="radio" name="gender" value="f" />Female <br>
  <br>
  <label for="fname">First name:</label><br>
  <input class="information" type="text" id="fname" name="fname" value="Jane"><br><br>
  <label for="lname">Last name:</label><br>
  <input class="information" type="text" id="lname" name="lname" value="Doe"><br><br>
  <label for="newsletter">Newsletter:</label>
  <input type="checkbox" name="newsletter" value="1" /><br><br>
  <input type="submit" value="Submit">
</form> 

<p>To know more about Selenium, visit the official page 
<a href ="www.selenium.dev">Selenium Official Page</a> 
</p>

</body>
</html>
```

# Nombre de la clase

El elemento web de la página HTML puede tener una clase de atributo. Podemos ver un ejemplo en el fragmento HTML que se muestra 
arriba. Podemos identificar estos elementos utilizando el localizador de nombres de clase disponible en Selenium.

```python
    driver = webdriver.Chrome()
 driver.find_element(By.CLASS_NAME, "information")
```
  
# Selector css

CSS es el lenguaje utilizado para diseñar páginas HTML. Podemos usar la estrategia del localizador del selector css para identificar 
el elemento en la página. Si el elemento tiene una identificación, creamos el localizador como css = #id. De lo contrario, el formato 
que seguimos es css =[attribute=value] . Veamos un ejemplo del fragmento HTML anterior. Crearemos un localizador para el cuadro de 
texto Nombre, usando css.

```python
    driver = webdriver.Chrome()
 driver.find_element(By.CSS_SELECTOR, "#fname")
```

# Identificación

Podemos usar el atributo ID disponible con elemento en una página web para localizarlo. Generalmente, la propiedad ID debe ser única 
para un elemento en la página web. Identificaremos el campo Apellido usándolo.

```python
    driver = webdriver.Chrome()
 driver.find_element(By.ID, "lname")
```

# Nombre
Podemos usar el atributo NOMBRE disponible con elemento en una página web para localizarlo. Generalmente, la propiedad NAME debe ser 
única para un elemento en la página web. Identificaremos la casilla de Newsletter usándola.

```python
    driver = webdriver.Chrome()
 driver.find_element(By.NAME, "newsletter")
```

# Texto del enlace

Si el elemento que queremos localizar es un enlace, podemos utilizar el localizador de texto de enlace para identificarlo en la 
página web. El texto del enlace es el texto que se muestra del enlace. En el fragmento de HTML compartido, tenemos un enlace 
disponible, veamos cómo lo ubicaremos.

```python
    driver = webdriver.Chrome()
 driver.find_element(By.LINK_TEXT, "Selenium Official Page")
```

# texto de enlace parcial

Si el elemento que queremos localizar es un enlace, podemos utilizar el localizador de texto de enlace parcial para identificarlo en 
la página web. El texto del enlace es el texto que se muestra del enlace. Podemos pasar texto parcial como valor. En el fragmento de 
HTML compartido, tenemos un enlace disponible, veamos cómo lo ubicaremos.

```python
    driver = webdriver.Chrome()
 driver.find_element(By.PARTIAL_LINK_TEXT, "Official Page")
```

# Nombre de la etiqueta

Podemos utilizar la propia ETIQUETA HTML como localizador para identificar el elemento web en la página. Desde el fragmento HTML 
anterior compartido, identifiquemos el enlace, usando su etiqueta html "a".

```python
    driver = webdriver.Chrome()
 driver.find_element(By.TAG_NAME, "a")
```

# Xpath

Un documento HTML puede considerarse como un documento XML, y luego podemos usar xpath, que será la ruta atravesada para llegar al 
elemento de interés para ubicar el elemento. El XPath podría ser un xpath absoluto, que se crea a partir de la raíz del documento. 
Ejemplo: /html/formulario/entrada[1]. Esto devolverá el botón de radio masculino. O el xpath podría ser relativo. Ejemplo- 
//input[@name='fname']. Esto devolverá el cuadro de texto del nombre. Vamos a crear un localizador para el botón de radio femenino
usando xpath.

```python
    driver = webdriver.Chrome()
 driver.find_element(By.XPATH, "//input[@value='f']")
```

# Localizadores relativos

Selenium 4 presenta localizadores relativos (anteriormente llamados localizadores amigables ). Estos localizadores son útiles cuando 
no es fácil construir un localizador para el elemento deseado, pero es fácil describir espacialmente dónde se encuentra el elemento 
en relación con un elemento que tiene un localizador fácilmente construido.

# Cómo funciona

Selenium usa la función de JavaScript getBoundingClientRect() para determinar el tamaño y la posición de los elementos en la página, 
y puede usar esta información para localizar elementos vecinos.

# Encontrar los elementos relativos.

Los métodos de localizador relativo pueden tomar como argumento para el punto de origen, ya sea una referencia de elemento 
previamente ubicada u otro localizador. En estos ejemplos, solo usaremos localizadores, pero podría intercambiar el localizador en el 
método final con un objeto de elemento y funcionará de la misma manera.

Consideremos el siguiente ejemplo para entender los localizadores relativos.

### Localizadores relativos

## Localizadores relativos disponibles

# Arriba

Si el elemento del campo de texto del correo electrónico no es fácilmente identificable por alguna razón, pero el elemento del campo 
de texto de la contraseña sí lo es, podemos ubicar el elemento del campo de texto usando el hecho de que es un elemento de "entrada" 
"arriba" del elemento de la contraseña.

```python
email_locator = locate_with(By.TAG_NAME, "input").above({By.ID: "password"})
```

# Abajo

Si el elemento del campo de texto de la contraseña no es fácilmente identificable por alguna razón, pero el elemento del campo de 
texto del correo electrónico sí lo es, podemos ubicar el elemento del campo de texto usando el hecho de que es un elemento de 
"entrada" "debajo" del elemento del correo electrónico.

```python
password_locator = locate_with(By.TAG_NAME, "input").below({By.ID: "email"})
```

# Izquierda de

Si el botón de cancelación no es fácilmente identificable por alguna razón, pero el elemento del botón de envío sí lo es, podemos 
ubicar el elemento del botón de cancelación usando el hecho de que es un elemento de "botón" a la "izquierda" del elemento de envío.


```python
cancel_locator = locate_with(By.TAG_NAME, "button").to_left_of({By.ID: "submit"})
```

# Derecho de

Si el botón de envío no es fácilmente identificable por algún motivo, pero el elemento del botón de cancelación sí lo es, podemos 
ubicar el elemento del botón de envío utilizando el hecho de que es un elemento de "botón" "a la derecha" del elemento de cancelación.

```python
submit_locator = locate_with(By.TAG_NAME, "button").to_right_of({By.ID: "cancel"})
```

# Cerca

Si el posicionamiento relativo no es obvio o varía según el tamaño de la ventana, puede usar el método cercano para identificar un 
elemento que esté como máximo 50pxalejado del localizador proporcionado. Un gran caso de uso para esto es trabajar con un elemento de 
formulario que no tiene un localizador fácil de construir, pero su elemento de etiqueta de entrada asociado sí lo tiene.

```python
email_locator = locate_with(By.TAG_NAME, "input").near({By.ID: "lbl-email"})
```

## Encadenamiento de localizadores relativos

También puede encadenar localizadores si es necesario. A veces, el elemento se identifica más fácilmente si se encuentra arriba/abajo 
de un elemento y a la derecha/izquierda de otro.

```python
submit_locator = locate_with(By.TAG_NAME, "button").below({By.ID: "email"}).to_right_of({By.ID: "cancel"})
```

### Interactuando con elementos web

Un conjunto de instrucciones de alto nivel para manipular controles de formulario.
Solo hay 5 comandos básicos que se pueden ejecutar en un elemento:

1. click (aplica a cualquier elemento)
2. send keys (solo se aplica a campos de texto y elementos editables de contenido)
3. clear (solo se aplica a campos de texto y elementos editables de contenido)
4. submit (solo se aplica a los elementos del formulario)
5. select (ver Elementos de la lista de selección)

# Validaciones adicionales

Estos métodos están diseñados para emular de cerca la experiencia de un usuario, por lo que, a diferencia de la API de acciones,
intenta realizar dos cosas antes de intentar la acción especificada.

Si determina que el elemento está fuera de la ventana gráfica, desplaza el elemento a la vista , específicamente alineará la parte 
inferior del elemento con la parte inferior de la ventana gráfica.
Se asegura de que el elemento sea interactuable antes de realizar la acción. Esto podría significar que el desplazamiento no tuvo 
éxito o que el elemento no se muestra de otra manera. Determinar si un elemento se muestra en una página era demasiado difícil de 
definir directamente en la especificación del controlador web , por lo que Selenium envía un comando de ejecución con un átomo de 
JavaScript que verifica las cosas que evitarían que se muestre el elemento. Si determina que un elemento no está en la ventana 
gráfica, no se muestra, no se puede interactuar con el teclado o no se puede interactuar con el puntero , devuelve un error de 
elemento que no se puede interactuar.

# Hacer clic

El comando de clic del elemento se ejecuta en el centro del elemento. Si el centro del elemento está oscurecido por algún motivo, 
Selenium devolverá un error de interceptación de clic en el elemento.

```python
# Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Click on the element 
driver.find_element(By.NAME, "color_input").click()
```

# Enviar claves

El comando de envío de claves del elemento escribe las claves proporcionadas en un elemento editable. Normalmente, esto significa que 
un elemento es un elemento de entrada de un formulario con un texttipo o un elemento con un content-editableatributo. Si no es 
editable, se devuelve un error de estado de elemento no válido.

Aquí está la lista de posibles pulsaciones de teclas que admite WebDriver.

```python
# Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Clear field to empty it from any previous data
driver.find_element(By.NAME, "email_input").clear()

# Enter Text
driver.find_element(By.NAME, "email_input").send_keys("admin@localhost.dev" )
```
  
# Clear (Limpiar)

El comando borrar elemento restablece el contenido de un elemento. Esto requiere que un elemento sea editable y reiniciable.
Normalmente, esto significa que un elemento es un elemento de entrada de un formulario con un texttipo o un elemento con un 
content-editableatributo. Si no se cumplen estas condiciones, se devuelve un error de estado de elemento no válido.

```python
# Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Clear field to empty it from any previous data
driver.find_element(By.NAME, "email_input").clear()
```
   
# Entregar

En Selenium 4, esto ya no se implementa con un punto final separado y funciona mediante la ejecución de un script. Como tal, se 
recomienda no utilizar este método y hacer clic en el botón de envío del formulario correspondiente.

### Información sobre elementos web

Lo que puedes aprender sobre un elemento.
Hay una serie de detalles que puede consultar sobre un elemento específico.

# Se visualiza

Este método se utiliza para comprobar si el elemento conectado se muestra en una página web. Devuelve un Booleanvalor, True si el 
elemento conectado se muestra en el contexto de navegación actual; de lo contrario, devuelve false.

Esta funcionalidad se menciona en la especificación w3c, pero no está definida por ella, debido a la imposibilidad de cubrir todas 
las condiciones potenciales . Como tal, Selenium no puede esperar que los controladores implementen esta funcionalidad directamente y
ahora se basa en la ejecución directa de una gran función de JavaScript. Esta función realiza muchas aproximaciones sobre la 
naturaleza y la relación de un elemento en el árbol para devolver un valor.

```python
# Navigate to the url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Get boolean value for is element display
is_email_visible = driver.find_element(By.NAME, "email_input").is_displayed()
```
# Está habilitado

Este método se utiliza para verificar si el elemento conectado está habilitado o deshabilitado en una página web. Devuelve un valor 
booleano, True si el elemento conectado está habilitado en el contexto de navegación actual; de lo contrario, devuelve false.

```python
# Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Returns true if element is enabled else returns false
value = driver.find_element(By.NAME, 'button_input').is_enabled()
```

# Es seleccionado

Este método determina si el Elemento al que se hace referencia está Seleccionado o no. Este método se usa ampliamente en casillas de 
verificación, botones de radio, elementos de entrada y elementos de opción.

Devuelve un valor booleano, True si el elemento al que se hace referencia está seleccionado en el contexto de navegación actual; de 
lo contrario, devuelve false.

```python
# Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Returns true if element is checked else returns false
value = driver.find_element(By.NAME, "checkbox_input").is_selected()
```
  
# Nombre de etiqueta

Se utiliza para obtener el nombre de etiqueta del elemento al que se hace referencia que tiene el foco en el contexto de navegación 
actual.

```python
# Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Returns TagName of the element
attr = driver.find_element(By.NAME, "email_input").tag_name
```
  
# Tamaño y Posición

Se utiliza para obtener las dimensiones y coordenadas del elemento al que se hace referencia.

El cuerpo de datos obtenido contiene los siguientes detalles:

- Posición del eje X desde la esquina superior izquierda del elemento
- Posición del eje y desde la esquina superior izquierda del elemento
- Altura del elemento
- Ancho del elemento

```python
# Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Returns height, width, x and y coordinates referenced element
res = driver.find_element(By.NAME, "range_input").rect
```

# Obtener valor CSS

Recupera el valor de la propiedad de estilo calculada especificada de un elemento en el contexto de exploración actual.

```python
# Navigate to Url
driver.get('https://www.selenium.dev/selenium/web/colorPage.html')

# Retrieves the computed style property 'color' of linktext
cssValue = driver.find_element(By.ID, "namedColor").value_of_css_property('background-color')
```
  
# Contenido del texto

Recupera el texto representado del elemento especificado.

```python
# Navigate to url
driver.get("https://www.selenium.dev/selenium/web/linked_image.html")

# Retrieves the text of the element
text = driver.find_element(By.ID, "justanotherlink").text
```

# Obtención de atributos o propiedades

Obtiene el valor de tiempo de ejecución asociado con un atributo DOM. Devuelve los datos asociados al atributo o propiedad DOM del 
elemento.

```python
# Navigate to the url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Identify the email text box
email_txt = driver.find_element(By.NAME, "email_input")

# Fetch the value property associated with the textbox
value_info = email_txt.get_attribute("value")
```

### Interacciones del navegador

## Obtener información del navegador

# Obtener título

Puede leer el título de la página actual desde el navegador:

```python
driver.title
```

# Obtener URL actual

Puede leer la URL actual desde la barra de direcciones del navegador usando:

```python
driver.current_url
```

## Navegación del navegador

# Navegar a

Lo primero que querrá hacer después de iniciar un navegador es abrir su sitio web. Esto se puede lograr en una sola línea:

```python
driver.get("https://selenium.dev")
```

# Atrás

Pulsando el botón Atrás del navegador:

```python
driver.back()
```

# Adelante

Pulsando el botón de avance del navegador:

```python
driver.forward()
```

# Actualizar

Actualizar la página actual:

```python
driver.refresh()
```

### Alertas, avisos y confirmaciones de JavaScript

WebDriver proporciona una API para trabajar con los tres tipos de mensajes emergentes nativos que ofrece JavaScript. Estas ventanas 
emergentes están diseñadas por el navegador y ofrecen una personalización limitada.

# Alertas

El más simple de estos se denomina alerta, que muestra un mensaje personalizado y un solo botón que descarta la alerta, etiquetado en 
la mayoría de los navegadores como OK. También se puede descartar en la mayoría de los navegadores presionando el botón Cerrar, pero 
esto siempre hará lo mismo que el botón Aceptar. Vea un ejemplo de alerta.

WebDriver puede obtener el texto de la ventana emergente y aceptar o descartar estas alertas.

```python
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See an example alert").click()

# Wait for the alert to be displayed and store it in a variable
alert = wait.until(expected_conditions.alert_is_present())

# Store the alert text in a variable
text = alert.text

# Press the OK button
alert.accept()
```

# Confirmar

Un cuadro de confirmación es similar a una alerta, excepto que el usuario también puede optar por cancelar el mensaje. Ver una 
muestra confirmar.

Este ejemplo también muestra un enfoque diferente para almacenar una alerta:

```python
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See a sample confirm").click()

# Wait for the alert to be displayed
wait.until(expected_conditions.alert_is_present())

# Store the alert in a variable for reuse
alert = driver.switch_to.alert

# Store the alert text in a variable
text = alert.text

# Press the Cancel button
alert.dismiss()
```

# Inmediato

Los avisos son similares a los cuadros de confirmación, excepto que también incluyen una entrada de texto. De manera similar a 
trabajar con elementos de formulario, puede usar las teclas de envío de WebDriver para completar una respuesta. Esto reemplazará 
completamente el texto del marcador de posición. Presionar el botón cancelar no enviará ningún texto. Vea un mensaje de muestra.

```python
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See a sample prompt").click()

# Wait for the alert to be displayed
wait.until(expected_conditions.alert_is_present())

# Store the alert in a variable for reuse
alert = Alert(driver)

# Type your message
alert.send_keys("Selenium")

# Press the OK button
alert.accept()
```

## Trabajando con cookies

Una cookie es una pequeña porción de datos que se envía desde un sitio web y se almacena en su computadora. Las cookies se utilizan 
principalmente para reconocer al usuario y cargar la información almacenada.

La API de WebDriver proporciona una forma de interactuar con las cookies con métodos integrados:

# Agregar galleta

Se utiliza para añadir una cookie al contexto de navegación actual. Add Cookie solo acepta un conjunto de objetos JSON serializables 
definidos. Aquí está el enlace a la lista de valores de clave JSON aceptados.

En primer lugar, debe estar en el dominio para el que la cookie será válida. Si está tratando de configurar las cookies antes de 
comenzar a interactuar con un sitio y su página de inicio es grande o tarda un poco en cargarse, una alternativa es encontrar una 
página más pequeña en el sitio (normalmente, la página 404 es pequeña, por ejemplo, http:// ejemplo .com/some404page)

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.example.com")

# Adds the cookie into current browser context
driver.add_cookie({"name": "key", "value": "value"})
```
  
# Obtener cookie con nombre

Devuelve los datos de la cookie serializados que coinciden con el nombre de la cookie entre todas las cookies asociadas.

```python
from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

# Adds the cookie into current browser context
driver.add_cookie({"name": "foo", "value": "bar"})

# Get cookie details with named cookie 'foo'
print(driver.get_cookie("foo"))
```
  
# Obtener todas las cookies

Devuelve 'datos de cookies serializados con éxito' para el contexto de navegación actual. Si el navegador ya no está disponible, 
devuelve un error.

```python
from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

# Get all available cookies
print(driver.get_cookies())
```
  
# Eliminar cookie

Elimina los datos de la cookie que coinciden con el nombre de la cookie proporcionada.

```python
from selenium import webdriver
driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")
driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

# Delete a cookie with name 'test1'
driver.delete_cookie("test1")
```
  
# Eliminar todas las cookies

Elimina todas las cookies del contexto de navegación actual.

```python
from selenium import webdriver
driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")
driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

#  Deletes all cookies
driver.delete_all_cookies()
```
  
# Atributo de cookie del mismo sitio

Permite al usuario indicar a los navegadores que controlen si se envían cookies junto con la solicitud iniciada por sitios de 
terceros. Se introduce para prevenir ataques CSRF (Cross-Site Request Forgery).

El atributo de cookie del mismo sitio acepta dos parámetros como instrucciones.

Estricto:
Cuando el atributo sameSite se establece como Strict , la cookie no se enviará junto con las solicitudes iniciadas por sitios web de 
terceros.

Flojo:
Cuando establece un atributo del mismo sitio de cookie en Lax, la cookie se enviará junto con la solicitud GET iniciada por un sitio 
web de terceros.

Nota: a partir de ahora, esta función está disponible en Chrome (versión 80+), Firefox (versión 79+) y funciona con Selenium 4 y 
versiones posteriores.

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.example.com")
# Adds the cookie into current browser context with sameSite 'Strict' (or) 'Lax'
driver.add_cookie({"name": "foo", "value": "value", 'sameSite': 'Strict'})
driver.add_cookie({"name": "foo1", "value": "value", 'sameSite': 'Lax'})
cookie1 = driver.get_cookie('foo')
cookie2 = driver.get_cookie('foo1')
print(cookie1)
print(cookie2)
```

## Trabajar con IFrames y marcos

Los marcos son un medio ahora en desuso para crear un diseño de sitio a partir de varios documentos en el mismo dominio. Es poco 
probable que trabaje con ellos a menos que esté trabajando con una aplicación web anterior a HTML5. Los iframes permiten la inserción 
de un documento de un dominio completamente diferente y todavía se usan comúnmente.

Si necesita trabajar con marcos o iframes, WebDriver le permite trabajar con ellos de la misma manera. Considere un botón dentro de 
un iframe. Si inspeccionamos el elemento utilizando las herramientas de desarrollo del navegador, es posible que veamos lo siguiente:

```html
<div id="modal">
  <iframe id="buttonframe" name="myframe"  src="https://seleniumhq.github.io">
   <button>Click here</button>
 </iframe>
</div>
```

Si no fuera por el iframe, esperaríamos hacer clic en el botón usando algo como:

```python
# This Wont work
driver.find_element(By.TAG_NAME, 'button').click()
```
  
Sin embargo, si no hay botones fuera del iframe, es posible que obtenga un error de elemento no . Esto sucede porque Selenium solo 
conoce los elementos en el documento de nivel superior. Para interactuar con el botón, primero debemos cambiar al marco, de manera 
similar a como cambiamos de ventana. WebDriver ofrece tres formas de cambiar a un marco.

# Uso de un elemento web

Cambiar usando un WebElement es la opción más flexible. Puede encontrar el marco usando su selector preferido y cambiar a él.

```python
# Store iframe web element
iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")

# switch to selected iframe
driver.switch_to.frame(iframe)

# Now click on button
driver.find_element(By.TAG_NAME, 'button').click()
```
  
# Usando un nombre o identificación

Si su marco o iframe tiene un atributo de identificación o nombre, se puede usar en su lugar. Si el nombre o ID no es único en la 
página, se cambiará al primero que se encuentre.

```python
# Switch frame by id
driver.switch_to.frame('buttonframe')

# Now, Click on the button
driver.find_element(By.TAG_NAME, 'button').click()
```
  
# Usando un índice

También es posible usar el índice del marco, como se puede consultar usando window.frames en JavaScript.

```python
# switching to second iframe based on index
iframe = driver.find_elements(By.TAG_NAME,'iframe')[1]

# switch to selected iframe
driver.switch_to.frame(iframe)
```  

# Dejando un marco

Para dejar un iframe o conjunto de marcos, vuelva al contenido predeterminado de la siguiente manera:

```python
# switch back to default content
driver.switch_to.default_content()
```

### Trabajar con ventanas y pestañas

## Ventanas y pestañas

# Obtener identificador de ventana

WebDriver no distingue entre ventanas y pestañas. Si su sitio abre una nueva pestaña o ventana, Selenium le permitirá trabajar con 
ella usando un identificador de ventana. Cada ventana tiene un identificador único que permanece persistente en una sola sesión. 
Puede obtener el identificador de ventana de la ventana actual usando:

```python
driver.current_window_handle
```

# Cambiar ventanas o pestañas

Al hacer clic en un enlace que se abre en una nueva ventana, se enfocará la nueva ventana o pestaña en la pantalla, pero WebDriver no
 sabrá qué ventana el sistema operativo considera activa. Para trabajar con la nueva ventana, deberá cambiar a ella. Si solo tiene 
 dos pestañas o ventanas abiertas y sabe con qué ventana comienza, mediante el proceso de eliminación puede recorrer ambas ventanas o 
 pestañas que puede ver WebDriver y cambiar a la que no es la original.

Sin embargo, Selenium 4 proporciona una nueva API NewWindow que crea una nueva pestaña (o) una nueva ventana y cambia automáticamente 
a ella.

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Firefox() as driver:
    # Open URL
    driver.get("https://seleniumhq.github.io")

    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Click the link which opens in a new window
    driver.find_element(By.LINK_TEXT, "new window").click()

    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Wait for the new tab to finish loading content
    wait.until(EC.title_is("SeleniumHQ Browser Automation"))
```
  
# Crear nueva ventana (o) nueva pestaña y cambiar

Crea una nueva ventana (o) pestaña y enfocará la nueva ventana o pestaña en la pantalla. No necesita cambiar para trabajar con la
nueva ventana (o) pestaña. Si tiene más de dos ventanas (o) pestañas abiertas además de la nueva ventana, puede recorrer ambas 
ventanas o pestañas que puede ver WebDriver y cambiar a la que no es la original.

Nota: Esta función funciona con Selenium 4 y versiones posteriores.

```python
# Opens a new tab and switches to new tab
driver.switch_to.new_window('tab')

# Opens a new window and switches to new window
driver.switch_to.new_window('window')
```
  
# Cerrar una ventana o pestaña

Cuando haya terminado con una ventana o pestaña y no sea la última ventana o pestaña abierta en su navegador, debe cerrarla y volver 
a la ventana que estaba usando anteriormente. Suponiendo que siguió el ejemplo de código en la sección anterior, tendrá el 
identificador de ventana anterior almacenado en una variable. Junta esto y obtendrás:

```python
#Close the tab or window
driver.close()

#Switch back to the old tab or window
driver.switch_to.window(original_window)
```
  
Si se olvida de volver a cambiar a otro identificador de ventana después de cerrar una ventana, WebDriver se ejecutará en la página 
ahora cerrada y activará una excepción de ventana no mencionada . Debe volver a cambiar a un identificador de ventana válido para 
continuar con la ejecución.

# Salir del navegador al final de una sesión

Cuando haya terminado con la sesión del navegador, debe llamar a salir, en lugar de cerrar:

```python
driver.quit()
```

Salir será:

1. Cierre todas las ventanas y pestañas asociadas con esa sesión de WebDriver
2. Cerrar el proceso del navegador
3. Cierre el proceso del controlador en segundo plano
4. Notifique a Selenium Grid que el navegador ya no está en uso para que otra sesión pueda usarlo (si está usando Selenium Grid)

Si no cancela la llamada, dejará procesos en segundo plano y puertos adicionales ejecutándose en su máquina, lo que podría causarle 
problemas más adelante.

Algunos marcos de prueba ofrecen métodos y anotaciones a los que puede conectarse para derribar al final de una prueba.

```python
# unittest teardown
# https://docs.python.org/3/library/unittest.html?highlight=teardown#unittest.TestCase.tearDown
def tearDown(self):
    self.driver.quit()
```
  
Si no ejecuta WebDriver en un contexto de prueba, puede considerar usar try / finallyel que ofrecen la mayoría de los lenguajes para 
que una excepción limpie la sesión de WebDriver.

```python
try:
    #WebDriver code here...
finally:
    driver.quit()
```
  
WebDriver de Python ahora es compatible con el administrador de contexto de Python, que al usar la with palabra clave puede cerrar 
automáticamente el controlador al final de la ejecución.

```python
with webdriver.Firefox() as driver:
  # WebDriver code here...

# WebDriver will automatically quit after indentation
```

# Gestión de ventanas

La resolución de la pantalla puede afectar la forma en que se representa su aplicación web, por lo que WebDriver proporciona 
mecanismos para mover y cambiar el tamaño de la ventana del navegador.

# Obtener el tamaño de la ventana

Obtiene el tamaño de la ventana del navegador en píxeles.

```python
# Access each dimension individually
width = driver.get_window_size().get("width")
height = driver.get_window_size().get("height")

# Or store the dimensions and query them later
size = driver.get_window_size()
width1 = size.get("width")
height1 = size.get("height")
```

# Establecer el tamaño de la ventana

Restaura la ventana y establece el tamaño de la ventana.

```python
driver.set_window_size(1024, 768)
```

# Obtener la posición de la ventana

Obtiene las coordenadas de la coordenada superior izquierda de la ventana del navegador.

```python
# Access each dimension individually
x = driver.get_window_position().get('x')
y = driver.get_window_position().get('y')

# Or store the dimensions and query them later
position = driver.get_window_position()
x1 = position.get('x')
y1 = position.get('y')
```
  
# Establecer la posición de la ventana

Mueve la ventana a la posición elegida.

```python
# Move the window to the top left of the primary monitor
driver.set_window_position(0, 0)
```
  
# Maximizar ventana

Amplía la ventana. Para la mayoría de los sistemas operativos, la ventana llenará la pantalla, sin bloquear los menús y las barras de 
herramientas del propio sistema operativo.

```python
driver.maximize_window()
```

# Minimizar ventana

Minimiza la ventana del contexto de navegación actual. El comportamiento exacto de este comando es específico de los administradores 
de ventanas individuales.

Minimizar ventana generalmente oculta la ventana en la bandeja del sistema.

Nota: Esta función funciona con Selenium 4 y versiones posteriores.

```python
driver.minimize_window()
```

# Ventana de pantalla completa

Llena toda la pantalla, similar a presionar F11 en la mayoría de los navegadores.

```python
driver.fullscreen_window()
```

# Tomar captura de pantalla

Se utiliza para realizar una captura de pantalla del contexto de navegación actual. La captura de pantalla del punto final de
WebDriver devuelve una captura de pantalla que está codificada en formato Base64.

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.example.com")

# Returns and base64 encoded string into image
driver.save_screenshot('./image.png')

driver.quit()
```

# Captura de pantalla de TakeElement

Se utiliza para capturar una captura de pantalla de un elemento para el contexto de navegación actual. La captura de pantalla del 
punto final de WebDriver devuelve una captura de pantalla que está codificada en formato Base64.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.example.com")

ele = driver.find_element(By.CSS_SELECTOR, 'h1')

# Returns and base64 encoded string into image
ele.screenshot('./image.png')

driver.quit()
```
  
# Ejecutar secuencia de comandos

Ejecuta un fragmento de código JavaScript en el contexto actual de un marco o ventana seleccionados.

```python
# Stores the header element
header = driver.find_element(By.CSS_SELECTOR, "h1")

# Executing JavaScript to capture innerText of header element
driver.execute_script('return arguments[0].innerText', header)
```

# Imprimir página

Imprime la página actual dentro del navegador.

Nota: Esto requiere que los navegadores Chromium estén en modo sin cabeza

```python
from selenium.webdriver.common.print_page_options import PrintOptions

print_options = PrintOptions()
print_options.page_ranges = ['1-2']

driver.get("printPage.html")

base64code = driver.print_page(print_options)
```

## IDE de selenio

Selenium IDE es una extensión del navegador que registra y reproduce las acciones de un usuario.
El entorno de desarrollo integrado de Selenium ( Selenium IDE ) es una extensión de navegador fácil de usar que registra las acciones 
de un usuario en el navegador utilizando los comandos existentes de Selenium, con parámetros definidos por el contexto de cada 
elemento. Proporciona una excelente manera de aprender la sintaxis de Selenium. Está disponible para Google Chrome, Mozilla Firefox y 
Microsoft Edge.

Para obtener más información, visite la documentación completa de Selenium IDE:

https://www.selenium.dev/selenium-ide/docs/en/introduction/getting-started

