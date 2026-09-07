# 🐍 Tienda Django

Una tienda web simple construida con **Django** y **Bootstrap 5**. Muestra productos por categoría (Electrónica, Juguetería y Ropa) y permite ver el detalle de cada producto en su propia página.

## ✨ Funcionalidades

- **Página de inicio** con las 3 secciones de la tienda.
- **Secciones** que listan los productos de cada categoría en tarjetas.
- **Detalle de producto** en una página independiente (`/producto/<id>/`).
- Diseño responsive con **Bootstrap 5**.

## 🚀 Cómo ejecutarlo

### 1. Clonar el repositorio

```bash
git clone https://github.com/Gatoco/django-tienda.git
cd django-tienda/ejercicioProyecto
```

### 2. Crear el entorno virtual e instalar Django

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install django
```

### 3. Migraciones (opcional, no hay modelos)

```bash
python manage.py migrate
```

### 4. Correr el servidor

```bash
python manage.py runserver
```

Abre **http://127.0.0.1:8000/** en tu navegador.

## 🗂️ Estructura del proyecto

```
ejercicioProyecto/
├── manage.py
├── ejercicioProyecto/          ← configuración (settings.py, urls.py)
├── ejercicioApp/               ← la app (views.py, models.py)
├── templates/
│   └── ejercicioApp/
│       ├── tienda.html         ← índice con botones
│       ├── seccion.html        ← tarjetas de productos
│       └── detalle.html        ← página de detalle de un producto
└── static/
    └── css/
        └── bootstrap.min.css   ← estilos
```

## 🧠 Cómo funciona

- **`views.py`** — cada sección arma un diccionario `data` con sus productos. La vista `detalleProducto` recibe un `id` por la URL, recorre la lista de productos y muestra el que coincide.
- **`urls.py`** — define las rutas, incluida `producto/<int:id_producto>/` para el detalle.
- **Templates** — usan el mini-lenguaje de Django (`{% url %}`, `{% for %}`, `{% if %}`) para pintar los datos.

## ⚙️ Configuración

Este proyecto está pensado como plantilla base. Para **adaptar el contenido a otro contexto** (por ejemplo, cambiar la tienda por una cartelera de cine) solo hay que tocar 3 lugares, siempre en el mismo orden:

### 1. Las secciones y productos → `ejercicioApp/views.py`

Cada vista de sección tiene su propio diccionario `data`. Ahí se cambian:

- El **nombre de la vista** (`electronica` → `accion`) y su `seccion` (el texto que aparece en el título).
- Los **productos** de la lista: `nombre`, `descripcion`, `precio`, `imagen` (de cada dict).
- El **nombre del archivo de template** si cambia (ej: `tienda.html` → `cartelera.html`).

> Importante: los `id` de los productos deben ser únicos en todo el proyecto, porque `detalleProducto` busca por `id`.

### 2. Las rutas → `ejercicioProyecto/urls.py`

Cada vista nueva se importa y se registra con su ruta y su `name=`:

```python
from ejercicioApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', miCartelera, name='miCartelera'),      # ← vista de inicio
    path('accion/', accion, name='accion'),          # ← una por sección
    path('comedia/', comedia, name='comedia'),
    path('drama/', drama, name='drama'),
    path('producto/<int:id_producto>/', detalleProducto, name='detalle'),
]
```

El `name=` de cada ruta se usa después en las templates con `{% url 'name' %}`. Si se renombra una ruta, hay que renombrarlo en las templates también.

### 3. Los textos y enlaces → `templates/ejercicioApp/`

En `tienda.html` (el índice):

- El **título** (`Mi tienda 🐍`) y el texto del header (`Secciones de la tienda`).
- Los **botones** de las secciones: cada uno apunta con `{% url 'electronica' %}` al name de su ruta. Si cambian las secciones, cambian el `{% url %}` y el texto del botón.

En `seccion.html` y `detalle.html`:

- El título `{{seccion}}` se llena solo desde la vista, no hay que tocarlo.
- El botón **"Ver detalles"** usa `{% url 'detalle' producto.id %}` — funciona igual para cualquier contexto.
- El botón **"Volver"** de `detalle.html` apunta a la primera sección (`{% url 'electronica' %}`) — se cambia por la sección que corresponda al nuevo contexto.

### Resumen rápido

| Qué cambia | Dónde |
|---|---|
| Nombre de vistas, `seccion` y productos | `views.py` |
| Rutas y `name=` | `urls.py` |
| Título, botones y textos | `tienda.html` |
| `{% url %}` de "Volver" en el detalle | `detalle.html` |
| Nombre de las templates | carpeta `templates/ejercicioApp/` (y las rutas en `views.py`) |

Con eso basta: el resto del proyecto (configuración, estáticos, detalle) es genérico y no cambia.

## 🛠️ Stack

- Python 3
- Django
- Bootstrap 5
