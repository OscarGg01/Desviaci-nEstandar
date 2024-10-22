import math
from typing import List

class NoSePuedeCalcular(Exception):
    pass

def calcular_media(elementos: List[float]) -> float:
    if not elementos:
        raise NoSePuedeCalcular("No se puede calcular la media de una lista vacía.")

    for elem in elementos:
        if not isinstance(elem, (int, float)):
            raise TypeError(f"El elemento {elem} no es numérico.")

    return sum(elementos) / len(elementos)

def calcular_desviacion_estandar(elementos: List[float]) -> float:
    if not elementos:
        raise NoSePuedeCalcular("No se puede calcular la desviación estándar de una lista vacía.")

    if len(elementos) == 1:
        return 0.0

    for elem in elementos:
        if not isinstance(elem, (int, float)):
            raise TypeError(f"El elemento {elem} no es numérico.")

    media = calcular_media(elementos)
    varianza = sum((x - media) ** 2 for x in elementos) / len(elementos)
    return math.sqrt(varianza)