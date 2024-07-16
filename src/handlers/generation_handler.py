import random as rd
import math
import string

import logging
from src.handlers.logger_handler import LoggerHandler

generation_logger_handler = LoggerHandler('/home/serwikk/Domotica/logs/generation_handler.log', 'generation_logger_handler' ,logging.INFO)

def agregar_umbral_a_valor(valor, umbral = 1):

    umbral_final = round(rd.uniform(umbral * -1, umbral), 2)

    valor_final = round(valor + umbral_final, 2)

    generation_logger_handler.logger.info(f"agregado el umbral {umbral_final} al valor {valor}, sumando el valor final de {valor_final}")

    return valor_final
    
#-------------------------------------------------------------------------------------------------------
# FUNCIÓN PARA LA GENERACIÓN DE IDs

def generar_id_aleatorio(prefijo = None, longitud=10):
    caracteres = string.ascii_letters + string.digits
    id_aleatorio = ''.join(rd.choices(caracteres, k=longitud))

    if prefijo:
        id_aleatorio = prefijo + id_aleatorio
    
    return id_aleatorio