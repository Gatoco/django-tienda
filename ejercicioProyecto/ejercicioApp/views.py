from django.shortcuts import render

def miTienda(request):
    return render(request, 'ejercicioApp/tienda.html')

def electronica(request):
    data = {
        'seccion': 'Electronica ⚡🔌',
        'productos': [
            {'id': 1, 'nombre': 'TV OLED', 'descripcion': 'Pantalla 55"', 'precio': '$1500', 'imagen': 'https://picsum.photos/200'},
            {'id': 2, 'nombre': 'Computador Gamer', 'descripcion': 'RTX 4090', 'precio': '$1800', 'imagen': 'https://picsum.photos/200'},
        ]
    }
    return render(request, 'ejercicioApp/seccion.html', data)

def jugueteria(request):
    data = {
        'seccion': 'Jugueteria 🧸🪁',
        'productos': [
            {'id': 3, 'nombre': 'Pelota', 'descripcion': 'De fútbol', 'precio': '$15', 'imagen': 'https://picsum.photos/200'},
            {'id': 4, 'nombre': 'Muñeca', 'descripcion': 'De trapo', 'precio': '$25', 'imagen': 'https://picsum.photos/200'},
        ]
    }
    return render(request, 'ejercicioApp/seccion.html', data)

def ropa(request):
    data = {
        'seccion': 'Ropa 👕👔',
        'productos': [
            {'id': 5, 'nombre': 'Polera', 'descripcion': 'Algodón', 'precio': '$20', 'imagen': 'https://picsum.photos/200'},
            {'id': 6, 'nombre': 'Jeans', 'descripcion': 'Mezclilla', 'precio': '$35', 'imagen': 'https://picsum.photos/200'},
        ]
    }
    return render(request, 'ejercicioApp/seccion.html', data)

def detalleProducto(request, id_producto):
    # Lista con TODOS los productos (como si fuera la base de datos)
    productos = [
        {'id': 1, 'nombre': 'TV OLED', 'descripcion': 'Pantalla 55"', 'precio': '$1500', 'imagen': 'https://picsum.photos/200'},
        {'id': 2, 'nombre': 'Computador Gamer', 'descripcion': 'RTX 4090', 'precio': '$1800', 'imagen': 'https://picsum.photos/200'},
        {'id': 3, 'nombre': 'Pelota', 'descripcion': 'De fútbol', 'precio': '$15', 'imagen': 'https://picsum.photos/200'},
        {'id': 4, 'nombre': 'Muñeca', 'descripcion': 'De trapo', 'precio': '$25', 'imagen': 'https://picsum.photos/200'},
        {'id': 5, 'nombre': 'Polera', 'descripcion': 'Algodón', 'precio': '$20', 'imagen': 'https://picsum.photos/200'},
        {'id': 6, 'nombre': 'Jeans', 'descripcion': 'Mezclilla', 'precio': '$35', 'imagen': 'https://picsum.photos/200'},
    ]
    # Busca el producto cuyo id coincida con el que llega por la URL
    producto = None
    for p in productos:
        if p['id'] == id_producto:
            producto = p
            break
    return render(request, 'ejercicioApp/detalle.html', {'producto': producto})
