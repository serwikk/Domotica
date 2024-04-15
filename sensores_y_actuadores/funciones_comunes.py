import random as rd
import csv
import os
import math


def generar_valor_distribucion_normal(media_dist_normal: float, desviacion_estandar: float, min_temp: float, max_temp: float) -> float:
    
    # Generar valor con distribución normal
    valor = rd.normalvariate(media_dist_normal, desviacion_estandar)

    # Ajuste del valor entre el rango incluido
    valor = max(min_temp, min(max_temp, valor))

    return valor


def generar_outlier(min_outlier: float, max_outlier: float) -> float:

    return rd.uniform(min_outlier, max_outlier)


def generar_valor_ciclico(hora: int, valor_min: float, valor_max: float, umbral: float = 0.7, fase: float = math.radians(170)) -> float:

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
