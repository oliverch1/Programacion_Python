#solamente utilice está celda para escribir todo su programa, si utiliza mas de una celda habrá descuento de puntaje.

import random

# En esta parte se ingresarán los equipos a participar
equipos = []

while True:
    # se usara .strip() para eliminar cualquier espacio ingresado antes y despues de nombre de pais ingesado
    # se usara .title() para convertir la primera letra en mayuscyla y el resto en minuscula, esto para tener mas orden
    equipo = input(f"Equipo {len(equipos) + 1}: ").strip().title()

    # Validamos que el equipo contenga solo letras y espacios, no se permitira el ingreso de numeros o caracteres especiales.
    if not all(nombre_correcto.isalpha() or nombre_correcto.isspace() for nombre_correcto in equipo):
        print("El nombre del equipo debe contener letras y espacios. Intente nuevamente.")
    elif equipo in equipos:
        print("El equipo ya se encuentra registrado, ingrese otro equipo.")
    else:
        equipos.append(equipo)

        # Preguntar si desea seguir agregando mas equipos
        while True:
            # se usa .lowe() para convertir la palabra ingresada a minuscula
            continuar = input("¿Desea registrar otro equipo s/n?: ").strip().lower()
            if continuar in ['s', 'n']:
                break
            else:
                print("Error. Ingrese 's' para sí o 'n' para no.")
        
        if continuar == 'n':
            print("¡Registro completado!")
            break


#--------------------------------------------------------------------------------------------------
# Se prosede a simular los encuentros de los equipos inscritos
resultados = []
for i in range(len(equipos)):
    for j in range(i + 1, len(equipos)):
        goles_equipo_1 = random.randint(0, 3)
        goles_equipo_2 = random.randint(0, 3)
        resultados.append((equipos[i], goles_equipo_1, equipos[j], goles_equipo_2))

# Aqui se muestra el resultado de los encuentros de los equipos 
print("\nResultados de los partidos:")
for partido in resultados:
    print(f"{partido[0]} {partido[1]} - {partido[2]} {partido[3]}")

#--------------------------------------------------------------------------------------------------
# Tabla inicial de los equipos inscritos con PG=0, PP=0, PE=0, GF=0, GC=0, PTOS=0 para todos 
tabla = [(equipo, 0, 0, 0, 0, 0, 0) for equipo in equipos]

# Actualizamos la tabla segun cada resultado de los partidos jugados por cada equipo
for partido in resultados:
    equipo1, goles1, equipo2, goles2 = partido
    
    # Buscamos un indice para los equipos con el fin de ubicarlos en la tabla y actualizar sus datos
    indice_equipo1 = [i for i in range(len(tabla)) if tabla[i][0] == equipo1][0]
    indice_equipo2 = [i for i in range(len(tabla)) if tabla[i][0] == equipo2][0]
    
    # Actualizamos los goles a favor y en contra
    tabla[indice_equipo1] = (tabla[indice_equipo1][0], tabla[indice_equipo1][1], tabla[indice_equipo1][2], tabla[indice_equipo1][3],
                             tabla[indice_equipo1][4] + goles1, tabla[indice_equipo1][5] + goles2, tabla[indice_equipo1][6])
    
    tabla[indice_equipo2] = (tabla[indice_equipo2][0], tabla[indice_equipo2][1], tabla[indice_equipo2][2], tabla[indice_equipo2][3],
                             tabla[indice_equipo2][4] + goles2, tabla[indice_equipo2][5] + goles1, tabla[indice_equipo2][6])
    
    # Actualizamos los partidos ganados, perdidos, empatados y puntos
    if goles1 > goles2:
        tabla[indice_equipo1] = (tabla[indice_equipo1][0], tabla[indice_equipo1][1] + 1, tabla[indice_equipo1][2], tabla[indice_equipo1][3],
                                 tabla[indice_equipo1][4], tabla[indice_equipo1][5], tabla[indice_equipo1][6] + 3)
        tabla[indice_equipo2] = (tabla[indice_equipo2][0], tabla[indice_equipo2][1], tabla[indice_equipo2][2] + 1, tabla[indice_equipo2][3],
                                 tabla[indice_equipo2][4], tabla[indice_equipo2][5], tabla[indice_equipo2][6])
    elif goles1 < goles2:
        tabla[indice_equipo1] = (tabla[indice_equipo1][0], tabla[indice_equipo1][1], tabla[indice_equipo1][2] + 1, tabla[indice_equipo1][3],
                                 tabla[indice_equipo1][4], tabla[indice_equipo1][5], tabla[indice_equipo1][6])
        tabla[indice_equipo2] = (tabla[indice_equipo2][0], tabla[indice_equipo2][1] + 1, tabla[indice_equipo2][2], tabla[indice_equipo2][3],
                                 tabla[indice_equipo2][4], tabla[indice_equipo2][5], tabla[indice_equipo2][6] + 3)
    else:
        tabla[indice_equipo1] = (tabla[indice_equipo1][0], tabla[indice_equipo1][1], tabla[indice_equipo1][2], tabla[indice_equipo1][3] + 1,
                                 tabla[indice_equipo1][4], tabla[indice_equipo1][5], tabla[indice_equipo1][6] + 1)
        tabla[indice_equipo2] = (tabla[indice_equipo2][0], tabla[indice_equipo2][1], tabla[indice_equipo2][2], tabla[indice_equipo2][3] + 1,
                                 tabla[indice_equipo2][4], tabla[indice_equipo2][5], tabla[indice_equipo2][6] + 1)

# Ordenamos la tabla de posiciones segun las condiciones: puntos --------- diferencia de goles ------- al azar
n = len(tabla)
for i in range(n):
    for j in range(0, n - i - 1):
        # Comparacion de puntos
        if tabla[j][6] < tabla[j + 1][6]:
            tabla[j], tabla[j + 1] = tabla[j + 1], tabla[j]
        # Si tienen los mismos puntos, comparamos la diferencia de goles
        elif tabla[j][6] == tabla[j + 1][6]:
            diferencia_goles_j = tabla[j][4] - tabla[j][5]
            diferencia_goles_j1 = tabla[j + 1][4] - tabla[j + 1][5]
            if diferencia_goles_j < diferencia_goles_j1:
                tabla[j], tabla[j + 1] = tabla[j + 1], tabla[j]
            # Si tienen la misma diferencia de goles, elegir al azar
            elif diferencia_goles_j == diferencia_goles_j1:
                if random.choice([True, False]):
                    tabla[j], tabla[j + 1] = tabla[j + 1], tabla[j]

#--------------------------------------------------------------------------------------------------------
# Mostramos la tabla de posiciones despues de haber ordenado
print(f"\n  {'Equipo':20} {'PG':>3} {'PP':>3} {'PE':>3} {'GF':>3} {'GC':>3} {'PTOS':>5}")
print(f"  {'='*46}")

for data in tabla:
    print(f"  {data[0]:20} {data[1]:3} {data[2]:3} {data[3]:3} {data[4]:3} {data[5]:3} {data[6]:5}")
