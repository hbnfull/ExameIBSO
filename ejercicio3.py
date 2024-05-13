import pandas as pd
from datetime import datetime, timedelta

# Paso 1: Extraer la información del CSV
df = pd.read_csv('Prueba_Promociones.csv')

# Paso 2: Obtener la entrada del usuario
fecha_inicio = input("Ingrese la fecha de inicio (formato YYYY-MM-DD): ")
fecha_fin = input("Ingrese la fecha de fin (formato YYYY-MM-DD): ")
categoria = input("Ingrese la categoría: ")
uso = input("Ingrese el uso: ")
sku = input("Ingrese el SKU: ")
porcentaje = input("Ingrese el porcentaje (en formato decimal): ")
inventario_inicial = input("Ingrese el inventario inicial: ")

# Validaciones
try:
    fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
    assert isinstance(categoria, str)
    assert isinstance(uso, str)
    assert isinstance(sku, str)
    porcentaje = float(porcentaje)
    inventario_inicial = int(inventario_inicial)
except ValueError:
    print("Error: Por favor, ingrese valores válidos.")
    exit()
except AssertionError:
    print("Error: 'categoria', 'uso' y 'sku' deben ser cadenas de texto.")
    exit()

# Paso 3: Agregar columna de número de semana
df['# de semana'] = df['Fecha'].apply(lambda x: x.isocalendar()[1])

# Paso 4: Aplicar el incremento %
rango_fechas = (df['Fecha'] >= fecha_inicio) & (df['Fecha'] <= fecha_fin)
uso_condicion = df['Uso'] == uso if uso else True
categoria_condicion = df['Categoría'] == categoria if categoria else True
modelo_condicion = df['Modelo'] != 'real'
df.loc[rango_fechas & uso_condicion & categoria_condicion & modelo_condicion, 'Piezas'] *= (1 + porcentaje)

# Paso 5: Generar nuevo DataFrame con información del SKU seleccionado
df_sku = df[df['SKU'] == sku].copy()
df_sku.reset_index(drop=True, inplace=True)

# Calcular inventario proyectado
df_sku['Inventario Proyectado'] = inventario_inicial - df_sku['Piezas'].cumsum()

# Encontrar la primera fecha en la que el inventario se vuelve negativo
fecha_negativa = df_sku.loc[df_sku['Inventario Proyectado'] < 0, 'Fecha'].min()

# Imprimir resultados
print("El inventario se vuelve negativo a partir de:", fecha_negativa)
print(df_sku)