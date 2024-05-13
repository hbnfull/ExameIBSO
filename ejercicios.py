diccionario = {"cdmx":[22,38,37,34,33,35,40],
               "monterrey":[40,38,42,43,39,38,40],
               "guadalajara":[40,38,42,38,33,34,39]}

ciudadAlta = max(diccionario, key=lambda x: sum(diccionario[x])/len(diccionario[x]))
ciudadBaja = min(diccionario, key=lambda x: sum(diccionario[x])/len(diccionario[x]))

for clave in diccionario:
    total=0
    mayor=0
    menor=0
    for numero in diccionario[clave]:
        total+=numero
        if mayor<numero:mayor=numero
        if menor>numero or menor==0:menor=numero
    print(clave, "promedio", total/7, "mayor", mayor, "menor", menor)

print("Ciudad con menos temperatura: " + ciudadBaja + " | Ciudad con mas temperatura: " + ciudadAlta)