import random as rd
import toml # type: ignore

def obtener_valores_config(sensor):

    ruta_archivo_conf = '/home/serwikk/Domotica/sensores-y-actuadores/'
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

