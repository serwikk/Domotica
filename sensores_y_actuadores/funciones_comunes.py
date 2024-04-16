import random as rd
import csv
import os
import math


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


def generar_valor_ciclico(hora: float, valor_min: float, valor_max: float, umbral: float = 0.7, fase: float = math.radians(170)) -> float:

    amplitud = (valor_max - valor_min) / 2
    valor_medio = (valor_max + valor_min) / 2

    angulo = (hora / 24) * 2 * math.pi - fase

    valor = valor_medio + amplitud * math.sin(angulo)

    umbral = rd.uniform((-1) * umbral, umbral)
    
    valor_final = round(valor + umbral, 2)
    
    return valor_final



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
