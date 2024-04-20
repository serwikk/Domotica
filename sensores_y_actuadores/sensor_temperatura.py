# import funciones_comunes as fc
import random as rd

# from config import TEMPERATURA_MIN, TEMPERATURA_MAX, HOY



class SensorTemperatura():

    def __init__(self, id, tipo, en_funcionamiento = True, unidad='c'):
        self.id = id
        self.tipo = tipo
        self.en_funcionamiento = en_funcionamiento
        self.unidad = unidad

    def obtener_temperatura(self, hora) -> float:

        """
        Obtiene la temperatura (en ºC) de la hora adjunta

        Args:
            hora (datetime): Hora sobre la que se recoge la temperatura

        Returns:
            float: Temperatura de la hora
        """

        return fc.generar_valor_ciclico(fc.hora_datetime_a_float(hora), TEMPERATURA_MIN, TEMPERATURA_MAX)


def main():

    sensor1 = SensorTemperatura(id = 'temp2324', tipo = 'sensor_temperatura1')



if __name__ == "__main__":
    main()