def obtener_valor(letra):
    # Obtener el valor de la letra en función de su posición en el alfabeto
    return ord(letra) - ord('a') + 1

def calcular_suma(cadena):
    suma = 0
    for letra in cadena:
        if letra.islower():
            suma += obtener_valor(letra)
        else:
            print(f"Error: La letra '{letra}' no es minúscula.")
            return None
    return suma

def pedir_entrada():
    cadena = input("Ingrese una cadena de letras minúsculas: ")
    if not cadena.isalpha():
        for i, caracter in enumerate(cadena, 1):
            if not caracter.islower():
                print(f"Cambia por una letra el numero '{caracter}' en la posición {i}.")
                return None
    for i, caracter in enumerate(cadena, 1):
            if not caracter.islower():
                print(f"Cambia a minúscula la letra '{caracter}' en la posición {i}.")
                return None
    return cadena

cadena = pedir_entrada()
while cadena is None:
    cadena = pedir_entrada()
suma = calcular_suma(cadena)
if suma is not None:
    print(f"La suma de los valores de las letras en la cadena es: {suma}")
