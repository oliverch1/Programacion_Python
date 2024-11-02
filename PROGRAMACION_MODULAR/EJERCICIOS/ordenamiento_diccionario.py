puerto = {'ocho':8, 'tres':3, 'dos':2, 'nueve':9, 'cinco':5}

prioridad = list(puerto.values())

prioridad.sort()

new_puerto = {}

for i in prioridad:
    for clave,valor in puerto.items():
        if i == valor:
            new_puerto[clave] = valor
        else:
            continue

print(new_puerto)