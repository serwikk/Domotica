import random as rd
import math
import string

#-------------------------------------------------------------------------------------------------------
# FUNCIONES PARA GENERACIÓN DE VALORES

def generar_valor_distribucion_normal(valor_minimo: float, valor_maximo: float) -> float:

    media = (valor_maximo + valor_minimo) / 2
    desviacion = (valor_maximo - valor_minimo) / 6 # Estándar, cambiar según contexto
    
    # Generar valor con distribución normal
    valor = rd.normalvariate(media, desviacion)

    return round(valor, 2)


def generar_outlier(min_outlier: float, max_outlier: float) -> float:

    return rd.uniform(min_outlier, max_outlier)


def generar_valor_ciclico(hora: float, valor_min: float, valor_max: float, umbral: float = 0.7, fase: float = math.radians(170)) -> float:

    amplitud = (valor_max - valor_min) / 2
    valor_medio = (valor_max + valor_min) / 2

    angulo = (hora / 24) * 2 * math.pi - fase

    valor = valor_medio + amplitud * math.sin(angulo)

    umbral = rd.uniform((-1) * umbral, umbral)
    
    valor_final = round(valor + umbral, 2)
    
    return valor_final
   
    
#-------------------------------------------------------------------------------------------------------
# FUNCIÓN PARA LA GENERACIÓN DE IDs

def generar_id_aleatorio(prefijo = None, longitud=10):
    caracteres = string.ascii_letters + string.digits
    id_aleatorio = ''.join(rd.choices(caracteres, k=longitud))

    if prefijo:
        id_aleatorio = prefijo + id_aleatorio
    
    return id_aleatorio