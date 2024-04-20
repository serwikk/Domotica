from sensores_y_actuadores import sensor_temperatura as st, sensor_humedad as sh, sensor_luz as sl

from sensores_y_actuadores.config import TEMPERATURA_MIN, TEMPERATURA_MAX, HOY, HUMEDAD_MIN, HUMEDAD_MAX

from simuladores import funciones_comunes as fc

import os
import json

class Controlador():

    def __init__(self, espacio, sensores= None):
        self.espacio = espacio
        self.id_controlador = fc.generar_id_aleatorio(f"contr-")
        self.sensores = sensores

    def obtener_nombres_sensores(self) -> list:

        lista_nombres_sensores = []
        
        for sensor in self.sensores:
            lista_nombres_sensores.append(sensor.tipo)

        return lista_nombres_sensores


    def inicializar_valores(self):
        directorio = "espacio_inmueble/"
        nombre_archivo = f"{directorio}valores_espacio.json"

        datos = {
                    "temperatura": fc.generar_valor_ciclico(fc.hora_datetime_a_float(HOY), TEMPERATURA_MIN, TEMPERATURA_MAX),
                    "humedad": fc.generar_valor_distribucion_normal(HUMEDAD_MIN, HUMEDAD_MAX),
                    "luz": 1000
                }

        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)      
            



def main():

    sensor_temperatura1 = st.SensorTemperatura(id = fc.generar_id_aleatorio("temp-"), tipo = 'sensor_temperatura')

    controlador = Controlador(espacio = "Habitación_1", sensores=[sensor_temperatura1])

    print(vars(controlador))

    controlador.inicializar_valores()


if __name__=="__main__":
    main()