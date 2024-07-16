import random as rd
import math
import string

def agregar_umbral_a_valor(valor, umbral = 1):

    return round(valor + rd.uniform(umbral * -1, umbral), 2)
    
#-------------------------------------------------------------------------------------------------------
# FUNCIÓN PARA LA GENERACIÓN DE IDs

def generar_id_aleatorio(prefijo = None, longitud=10):
    caracteres = string.ascii_letters + string.digits
    id_aleatorio = ''.join(rd.choices(caracteres, k=longitud))

    if prefijo:
        id_aleatorio = prefijo + id_aleatorio
    
    return id_aleatorio