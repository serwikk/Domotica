from sensores_y_actuadores import sensor_temperatura as st, sensor_humedad as sh, sensor_luz as sl

from simuladores.config import TEMPERATURA_MIN, TEMPERATURA_MAX, HOY, HUMEDAD_MIN, HUMEDAD_MAX

from simuladores import funciones_comunes as fc

import os
import json

class Controlador():

    def __init__(self, espacio, sensores= []):
        self.espacio = espacio
        self.id_controlador = fc.generar_id_aleatorio(f"contr-")
        self.sensores = sensores
        self.lista_nombres_sensores = self.obtener_nombres_sensores()


    def obtener_nombres_sensores(self) -> list:

        lista_nombres_sensores = []
        
        for sensor in self.sensores:
            lista_nombres_sensores.append("sensor_"+sensor.magnitud)

        return lista_nombres_sensores


    def inicializar_valores(self) -> None:
        directorio = "espacio_inmueble/"
        nombre_archivo = f"{directorio}valores_espacio.json"

        datos = {
                    "temperatura": fc.generar_valor_ciclico(fc.hora_datetime_a_float(HOY), TEMPERATURA_MIN, TEMPERATURA_MAX),
                    "humedad": fc.generar_valor_distribucion_normal(HUMEDAD_MIN, HUMEDAD_MAX),
                    "luz": 1000
                }

        try:
            with open(nombre_archivo, 'w') as archivo:
                json.dump(datos, archivo, indent=4)      
        
        except:
            raise e