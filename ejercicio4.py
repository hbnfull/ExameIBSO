import requests

def obtener_best_sellers():
    try:
        # Pedir al usuario que elija la lista de "Best Sellers" a consultar
        opcion = input("¿Qué lista de 'Best Sellers' deseas consultar? (actual/especifica): ").lower()
        if opcion not in ['actual', 'especifica']:
            raise ValueError("Opción no válida.")

        # Si elige consultar una fecha específica, pedir la fecha
        fecha = None
        if opcion == 'especifica':
            fecha = input("Ingrese la fecha en formato YYYY-MM-DD: ")

        # Pedir al usuario un precio específico del libro
        precio = input("Ingrese el precio específico del libro (dejar en blanco para no filtrar por precio): ")
        precio = float(precio) if precio else None

        # Pedir al usuario un rango de edades dirigido para el libro
        rango_edades = input("Ingrese el rango de edades dirigido para el libro (dejar en blanco para no filtrar por edad): ")

        # Construir la URL de la API
        if opcion == 'actual':
            url = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json"
        else:
            url = f"https://api.nytimes.com/svc/books/v3/lists/{fecha}/hardcover-fiction.json"

        # Parámetros de la solicitud
        params = {'api-key': api_key}

        # Realizar la solicitud GET
        response = requests.get(url, params=params)

        # Verificar el estado de la respuesta
        if response.status_code == 200:
            # La solicitud fue exitosa
            data = response.json()
            # Aquí puedes trabajar con los datos devueltos
            return data, precio, rango_edades
        else:
            # La solicitud falló
            print("Error al realizar la solicitud:", response.status_code)
            return None, None, None
    except ValueError as e:
        print("Error:", e)
        return None, None, None

def filtrar_libros(data, precio, rango_edades):
    if data is None:
        return None
    libros_filtrados = []
    for libro in data['results']['books']:
        if precio is not None and libro['price'] != precio:
            continue
        if rango_edades and libro['age_group'] != rango_edades:
            continue
        libros_filtrados.append(libro)
    return libros_filtrados

# Definir la clave de la API
api_key = "1USeyekZQ42A6Yb48DlbGCORGY9EicYD"

# Obtener la lista de Best Sellers y los filtros del usuario
data, precio, rango_edades = obtener_best_sellers()

# Filtrar los libros según los criterios del usuario
libros_filtrados = filtrar_libros(data, precio, rango_edades)

# Imprimir los libros filtrados
if libros_filtrados:
    print("Libros filtrados:")
    for libro in libros_filtrados:
        print(f"- Título: {libro['title']}, Precio: {libro['price']}, Edad: {libro['age_group']}")
else:
    print("No se encontraron libros que cumplan con los criterios de búsqueda.")