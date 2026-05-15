# Tarea 1 - Levantar una aplicacion Flask desde cero

## Objetivo tecnico

Poner en marcha el proyecto en tu entorno local, entender para que sirve cada pieza minima del setup y verificar que la aplicacion responde en el navegador.

En esta primera clase no alcanza con "hacerlo andar". Tienes que empezar a distinguir que problema resuelve cada paso: aislamiento del entorno, instalacion de dependencias, arranque del servidor y renderizado de una plantilla HTML.

## Preparacion

Para instalar dependencias y ejecutar el proyecto, sigue el `README.md`.

## Consigna

1. Instala las dependencias y levanta la aplicacion siguiendo el `README.md`.

2. Abre la aplicacion en el navegador y comprueba que responde correctamente.

3. Modifica la vista base y verifica el cambio:

   Edita `templates/index.html`, cambia al menos el `<title>` y el `<h1>`, guarda y recarga la pagina.

   Este paso existe para que veas la relacion concreta entre archivo fuente, servidor y resultado en navegador. Codigo que no observas, no lo entendes.

## Preguntas de reflexion tecnica

1. Que problema concreto resuelve el entorno virtual en un proyecto Python?
El entorno virtual (.venv) aísla las dependencias de un proyecto para que no interfieran con otros proyectos ni con la instalación global de Python.

Por ejemplo:

Un proyecto puede usar Flask 2.3
Otro puede necesitar Flask 1.1

Sin entorno virtual, ambas versiones chocarían en tu sistema. Con .venv, cada proyecto tiene sus propias librerías y versiones.

RESPUESTA:

El entorno virtual (.venv) sirve para aislar las dependencias de un proyecto y evitar conflictos con otros proyectos o con Python instalado globalmente en el sistema.
Por ejemplo, un proyecto puede necesitar Flask 2.3 y otro Flask 1.1. Sin un entorno virtual, ambas versiones entrarían en conflicto. Con .venv, cada proyecto tiene sus propias librerías y versiones independientes.

2. Que diferencia hay entre instalar `Flask` globalmente y hacerlo dentro de `.venv`?

Instalación global:
Flask queda disponible para todo el sistema.
Puede generar conflictos entre proyectos.
Es más difícil reproducir el entorno en otra máquina.
Instalación dentro de .venv:
Flask solo existe dentro de ese proyecto.
Las dependencias quedan controladas y aisladas.
El proyecto es más portable y profesional.

En proyectos reales, casi siempre se usa .venv.


RESPUESTA:

Instalación global:

Flask queda disponible para todo el sistema.
Puede generar conflictos entre proyectos.
Hace más difícil reproducir el entorno en otra máquina.

Instalación dentro de .venv:

Flask solo existe dentro de ese proyecto.
Las dependencias quedan aisladas y organizadas.
El proyecto es más portable y profesional.

Por eso, en proyectos reales casi siempre se usa .venv.


3. Por que `requirements.txt` forma parte del proyecto y no de tu maquina personal?

Porque describe las dependencias necesarias para ejecutar el proyecto, no las de tu computadora.

Ese archivo permite que otra persona haga:

pip install -r requirements.txt

y obtenga exactamente las mismas librerías y versiones necesarias para que el proyecto funcione igual.

Es parte de la configuración del proyecto y normalmente se sube al repositorio.


RESPUESTA:

Porque ese archivo describe las dependencias necesarias para ejecutar el proyecto, no las de la computadora del desarrollador.

Gracias a requirements.txt, otra persona puede instalar exactamente las mismas librerías usando:

pip install -r requirements.txt

Así el proyecto funcionará igual en cualquier máquina. Por eso normalmente se guarda en el repositorio.


4. Cuando ejecutas `python app.py`, que archivo actua como punto de entrada y por que?

El archivo app.py actúa como punto de entrada porque es el archivo que Python ejecuta primero.

Allí normalmente:

se crea la aplicación Flask,
se definen las rutas,
y se inicia el servidor con algo como:
app.run(debug=True)

Todo comienza desde ese archivo.


RESPUESTA:

El archivo app.py actúa como punto de entrada porque es el primer archivo que Python ejecuta.

En ese archivo normalmente:

se crea la aplicación Flask,
se definen las rutas,
y se inicia el servidor con:
app.run(debug=True)

Todo el proyecto comienza desde ese archivo.


5. Que relacion hay entre la ruta `/`, la funcion `inicio()` y el archivo `templates/index.html`?

La relación es el flujo principal de Flask:

El navegador entra a la ruta /

RESPUESTA:

La relación representa el flujo principal de Flask:

El usuario entra a la ruta /.
Flask ejecuta la función inicio().
La función devuelve el archivo templates/index.html.
El navegador muestra ese HTML al usuario.

La ruta conecta al navegador con la función, y la función conecta con el archivo HTML.

6. Que evidencia te da la terminal de que el servidor arranco correctamente?

Flask normalmente muestra mensajes como:

* Running on http://127.0.0.1:5000

o:

* Debug mode: on

Eso indica que:

el servidor inició,
Flask está escuchando conexiones,
y puedes abrir esa dirección en el navegador.


RESPUESTA:

Flask normalmente muestra mensajes como:

* Running on http://127.0.0.1:5000

o:

* Debug mode: on

Eso significa que:

el servidor inició correctamente,
Flask está escuchando conexiones,
y la aplicación ya puede abrirse desde el navegador.


7. Si cambias el HTML y el navegador muestra otra cosa, que te demuestra eso sobre el flujo entre backend y frontend en este proyecto?


RESPUESTA:

Demuestra que existe una conexión entre el backend (Flask en Python) y el frontend (HTML mostrado en el navegador).

El flujo funciona así:

El navegador hace una petición.
Flask recibe la petición.
Flask envía el archivo HTML.
El navegador renderiza el contenido.

Si modificas el HTML y ves cambios en pantalla, significa que el backend está entregando correctamente la información al frontend.

## Entregable

La tarea se considera completa si puedes demostrar estas cuatro cosas:

1. El entorno virtual esta creado y activado.
2. Las dependencias se instalaron desde `requirements.txt`.
3. La aplicacion corre en tu maquina y responde en el navegador.
4. Modificaste `templates/index.html` y podes señalar exactamente donde se refleja ese cambio.

## Cierre

No estas aprendiendo a tipear comandos. Estas empezando a construir criterio tecnico. Si hoy entiendes que levanta el servidor, de donde salen las dependencias y por que Flask encuentra esa plantilla, entonces arrancaste bien. Simple no significa superficial.
