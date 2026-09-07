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

## 🛠️ Stack

- Python 3
- Django
- Bootstrap 5
