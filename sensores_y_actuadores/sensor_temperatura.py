from simuladores import funciones_comunes as fc

from sensores_y_actuadores.sensor import Sensor


class SensorTemperatura(Sensor):

    def __init__(self, en_funcionamiento = True, unidad='c'):

        super().__init__( id= fc.generar_id_aleatorio("temp-"), magnitud = "temperatura", en_funcionamiento = en_funcionamiento, unidad = unidad)

    def obtener_temperatura(self) -> float:

        """
        Obtiene la temperatura (en ºC) de la hora indicada

        Args:
            hora (datetime): Hora sobre la que se recoge la temperatura

        Returns:
            float: Temperatura de la hora
        """

        return fc.leer_valor_magnitud("temperatura", "./espacio_inmueble/valores_espacio.json")