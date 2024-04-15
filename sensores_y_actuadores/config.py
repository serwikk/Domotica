import toml
from datetime import datetime

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

(TEMPERATURA_MIN, TEMPERATURA_MAX) = obtener_valores_config('sensor_temperatura')
(HUMEDAD_MIN, HUMEDAD_MAX) = obtener_valores_config('sensor_humedad')
HOY = datetime.now()