lista_diccionarios = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "Ana", "edad": 22},
    {"nombre": "Juan", "edad": 30}
]

lista_sin_duplicados = []
vistos = set()

for datos in lista_diccionarios:
    tupla_datos = tuple(datos.items())
    if tupla_datos not in vistos:
        vistos.add(tupla_datos)
        lista_sin_duplicados.append(datos)
    else:
        continue

print(lista_sin_duplicados)
