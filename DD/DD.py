import math
import random
import time

class Paralelogramo:
    def __init__(self, ladoAB=1, ladoDA=1, anguloA=90):
        self.ladoAB = ladoAB
        self.ladoDA = ladoDA
        self.anguloA = anguloA

    def __repr__(self):
        # Representación textual del objeto
        return f"[Paralelogramo, ladoAB={self.ladoAB:.1f}, ladoDA={self.ladoDA:.1f}, anguloA={self.anguloA:.1f}]"

    # Decorador y validación para ladoAB
    @property
    def ladoAB(self):
        return self.__ladoAB

    @ladoAB.setter
    def ladoAB(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("El lado AB debe ser un número.")
        if val <= 0:
            raise ValueError("El lado AB debe ser mayor a cero.")
        self.__ladoAB = val

    # Decorador y validación para ladoDA
    @property
    def ladoDA(self):
        return self.__ladoDA

    @ladoDA.setter
    def ladoDA(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("El lado DA debe ser un número.")
        if val <= 0:
            raise ValueError("El lado DA debe ser mayor a cero.")
        self.__ladoDA = val

    # Decorador y validación para anguloA
    @property
    def anguloA(self):
        return self.__anguloA

    @anguloA.setter
    def anguloA(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("El ángulo A debe ser un número.")
        if not (0 < val < 180):
            raise ValueError("El ángulo A debe estar en el intervalo abierto (0, 180).")
        self.__anguloA = val

    def perimetro(self):
        return round(2 * (self.ladoAB + self.ladoDA), 1)

    def area(self):
        # Cálculo del área usando el seno del ángulo
        return round(self.ladoAB * self.ladoDA * math.sin(math.radians(self.anguloA)), 1)

    def es_cuadrado(self):
        return self.ladoAB == self.ladoDA and self.anguloA == 90

    def es_rectangulo(self):
        return self.anguloA == 90


# Programa de aplicación

# Generar lista de 40 paralelogramos con valores aleatorios para los lados y el ángulo
paralelogramos = [
    Paralelogramo(
        ladoAB=random.randint(10, 80),
        ladoDA=random.randint(10, 80),
        anguloA=random.randint(45, 120)
    )
    for _ in range(40)
]

# Imprimir la representación de los 40 objetos
print("Los 40 objetos de la lista:\n")
for p in paralelogramos:
    print(p)

# Calcular estadísticas
areas = [p.area() for p in paralelogramos]
perimetros = [p.perimetro() for p in paralelogramos]

promedio_areas = round(sum(areas) / len(areas), 1)
promedio_perimetros = round(sum(perimetros) / len(perimetros), 1)
mayor_area = max(areas)
mayor_perimetro = max(perimetros)

# Mostrar el reporte estadístico
print("\nReporte estadístico:\n")
print(f"Promedio de áreas: {promedio_areas}")
print(f"Promedio de perímetros: {promedio_perimetros}")
print(f"Mayor área calculada: {mayor_area}")
print(f"Mayor perímetro calculado: {mayor_perimetro}\n")

# Imprimir paralelogramos con área por encima del promedio
print("Paralelogramos cuya área está por encima del promedio:\n")
for p in paralelogramos:
    if p.area() > promedio_areas:
        print(p)