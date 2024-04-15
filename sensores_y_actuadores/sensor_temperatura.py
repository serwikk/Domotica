import funciones_comunes as fc
import random as rd

from config import TEMPERATURA_MIN, TEMPERATURA_MAX


def obtener_temperatura(hora):
    return fc.generar_valor_ciclico(hora, TEMPERATURA_MIN, TEMPERATURA_MAX)


def main():

    hora = 12
    valor = obtener_temperatura(hora)
 
    return valor




if __name__ == "__main__":
    main()