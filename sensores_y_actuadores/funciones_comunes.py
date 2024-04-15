import random as rd
import toml # type: ignore
import csv
import os
import math


def obtener_valores_config(sensor):

    ruta_archivo_conf = '/home/serwikk/Domotica/sensores_y_actuadores'
    try:
        with open(f'{ruta_archivo_conf}/conf.toml', 'r') as file:
            configuracion = toml.load(file)

        valores_sensor = configuracion[sensor]

        return valores_sensor.values()

    except Exception as e:

        print(f"Ha ocurrido un error de tipo: {e}") # En un futuro, cambiarlo por un registro de logs
        raise e

def generar_valor_distribucion_normal(media_dist_normal: float, desviacion_estandar: float, min_temp: float, max_temp: float) -> float:
    
    # Generar valor con distribución normal
    valor = rd.normalvariate(media_dist_normal, desviacion_estandar)

    # Ajuste del valor entre el rango incluido
    valor = max(min_temp, min(max_temp, valor))

    return valor


def generar_outlier(min_outlier: float, max_outlier: float) -> float:

    return rd.uniform(min_outlier, max_outlier)

def generar_valor_ciclico(hora: int, valor_min: float, valor_max: float) -> float:

    amplitud = (valor_max - valor_min) / 2
    valor_medio = (valor_max + valor_min) / 2

    angulo = (hora / 24) * 2 * math.pi

    valor = valor_medio + amplitud * math.sin(angulo)

    return round(valor, 2)



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
