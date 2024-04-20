import random as rd
import csv
import os
import math
import string
import json


def hora_datetime_a_float(hora: float) -> float:
    hora_float = hora.hour + hora.minute / 60

    return round(hora_float, 2)

def generar_valor_distribucion_normal(valor_minimo: float, valor_maximo: float) -> float:

    media = (valor_maximo + valor_minimo) / 2
    desviacion = (valor_maximo - valor_minimo) / 6 # Estándar, cambiar según contexto
    
    # Generar valor con distribución normal
    valor = rd.normalvariate(media, desviacion)

    return round(valor, 2)


def generar_outlier(min_outlier: float, max_outlier: float) -> float:

    return rd.uniform(min_outlier, max_outlier)

def generar_valor_ciclico(hora: int, valor_min: float, valor_max: float) -> float:

    amplitud = (valor_max - valor_min) / 2
    valor_medio = (valor_max + valor_min) / 2

    angulo = (hora / 24) * 2 * math.pi

    valor = valor_medio + amplitud * math.sin(angulo)

    return round(valor, 2)


def generar_valor_ciclico(hora: float, valor_min: float, valor_max: float, umbral: float = 0.7, fase: float = math.radians(170)) -> float:

    amplitud = (valor_max - valor_min) / 2
    valor_medio = (valor_max + valor_min) / 2

    angulo = (hora / 24) * 2 * math.pi - fase

    valor = valor_medio + amplitud * math.sin(angulo)

    umbral = rd.uniform((-1) * umbral, umbral)
    
    valor_final = round(valor + umbral, 2)
    
    return valor_final
    

def generar_id_aleatorio(prefijo = None, longitud=10):
    caracteres = string.ascii_letters + string.digits
    id_aleatorio = ''.join(rd.choices(caracteres, k=longitud))

    if prefijo:
        id_aleatorio = prefijo + id_aleatorio
    
    return id_aleatorio


def registrar_en_csv(ruta, campos, dato_nuevo):

     # Verificar si el archivo ya existe
    if not os.path.exists(ruta):
        # Si el archivo no existe, escribir los encabezados
        with open(ruta, 'w', newline='') as file:
            escritor = csv.DictWriter(file, fieldnames=campos)
            escritor.writeheader()
        
    with open(ruta, 'a', newline='') as file:
        csvwriter = csv.DictWriter(file, fieldnames=campos)

        csvwriter.writerow(dato_nuevo)

    print("Registro guardado correctamente en", ruta)

def leer_valor_magnitud(magnitud, direccion_archivo):
    
    with open(direccion_archivo, 'r') as archivo:

        datos = json.load(archivo)

    return datos[magnitud]