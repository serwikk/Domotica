import funciones_comunes as fc
import random as rd

from config import TEMPERATURA_MIN, TEMPERATURA_MAX, HOY


def obtener_temperatura(hora) -> float:

    """
    Obtiene la temperatura (en ºC) de la hora adjunta

    Args:
        hora (datetime): Hora sobre la que se recoge la temperatura

    Returns:
        float: Temperatura de la hora
    """

    return fc.generar_valor_ciclico(fc.hora_datetime_a_float(hora), TEMPERATURA_MIN, TEMPERATURA_MAX)


def main():

    valor = obtener_temperatura(HOY)

    return valor



if __name__ == "__main__":
    main()