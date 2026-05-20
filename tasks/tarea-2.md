# Tarea 2 - Datos dinamicos en una plantilla Flask

## Objetivo tecnico

Pasar datos desde `app.py` hacia `templates/index.html` usando `render_template`.
La meta es que el HTML no sea fijo: debe mostrar informacion enviada por Python.

## Preparacion

1. Asegurate de tener el proyecto funcionando (ver `README.md`).
2. Levanta la app y deja abierto el navegador en `http://127.0.0.1:5000/`.

## Guia paso a paso

### Paso 1: Revisar el punto de partida

Abre `app.py` y ubica la ruta `/`.
Deberias ver una funcion que retorna algo parecido a:

```python
return render_template("index.html")
```

Ese retorno todavia no envia datos.

### Paso 2: Definir variables en Python

Dentro de la funcion de la ruta `/`, crea al menos 3 variables.
Ejemplo:

```python
titulo = "Panel de inicio"
usuario = "Ana"
mensaje = "Bienvenida a Flask"
```

Puedes usar otros nombres y valores, pero deben tener sentido en la pagina.

### Paso 3: Enviar variables a la plantilla

Modifica `render_template` para pasar esas variables:

```python
return render_template(
    "index.html",
    titulo=titulo,
    usuario=usuario,
    mensaje=mensaje
)
```

Regla importante: el nombre a la izquierda (`titulo=`) es el nombre que usaras en HTML.

### Paso 4: Mostrar variables en `index.html`

Abre `templates/index.html` y agrega las variables con Jinja2:

```html
<title>{{ titulo }}</title>
<h1>{{ mensaje }}</h1>
<p>Usuario activo: {{ usuario }}</p>
```

Minimo requerido: mostrar 3 variables en lugares visibles de la pagina.

### Paso 5: Guardar y verificar

1. Guarda `app.py` y `templates/index.html`.
2. Recarga el navegador.
3. Comprueba que aparecen los valores que enviaste desde Python.

Si cambias un valor en `app.py` y se refleja en la pagina, lo hiciste bien.

## Checklist de validacion

Marca cada punto antes de entregar:

1. La ruta `/` en `app.py` fue modificada.
2. `render_template` recibe al menos 3 variables.
3. `index.html` muestra esas 3 variables con `{{ ... }}`.
4. El resultado se ve correctamente en el navegador.

## Errores comunes (y como corregirlos)

1. Error de nombre: en Python envias `usuario`, pero en HTML escribes `{{ user }}`.
   Solucion: usa exactamente el mismo nombre.
2. Olvidar llaves dobles: escribir `{ usuario }` en vez de `{{ usuario }}`.
   Solucion: siempre usar doble llave en Jinja2.
3. Editar archivo incorrecto o no guardar cambios.
   Solucion: verifica que editaste `templates/index.html` y guarda ambos archivos.

## Preguntas de reflexion tecnica

1. Que ventaja tiene cambiar datos desde `app.py` sin tocar todo el HTML?

RESPUESTA:

-Contenido dinámico: Permite mostrar información actualizada en tiempo real (ej. precios, clima, usuarios) sin editar el archivo HTML.
-Reutilización de código: Un solo archivo HTML puede servir para miles de productos distintos simplemente cambiando los datos que recibe desde Python.
-Separación de responsabilidades: Separa la lógica de negocios del diseño visual, facilitando el mantenimiento.


2. Que diferencia hay entre una variable definida en Python y una variable mostrada en Jinja2?

RESPUESTA:

-Variable en Python: Es un espacio de memoria donde el servidor procesa y almacena datos utilizando las reglas de tipado y lógica de Python.
-Variable en Jinja2: Se escribe entre llaves dobles {{ }} dentro del archivo HTML. Es una instrucción que le indica al motor de plantillas que debe reemplazar ese espacio por el valor que Python le envió al momento de renderizar la página

3. Si borras una variable de `render_template`, que parte visual deja de funcionar?


RESPUESTA:

Si eliminas una variable de la función render_template (en el archivo app.py) pero la sigues llamando en el HTML con {{ variable }}, solo dejará de verse el valor específico de esa variable.

## Entregable

Debes entregar:

1. `app.py` actualizado.
2. `templates/index.html` actualizado.
3. Evidencia minima:
   - Lista de las 3 variables usadas.
   - En que linea o seccion del HTML se muestra cada una.
