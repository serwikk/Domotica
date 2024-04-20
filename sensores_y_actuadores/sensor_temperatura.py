from simuladores import funciones_comunes as fc


class SensorTemperatura():

    def __init__(self, en_funcionamiento = True, unidad='c'):
        self.id = fc.generar_id_aleatorio("temp-")
        self.magnitud = "temperatura"
        self.en_funcionamiento = en_funcionamiento
        self.unidad = unidad

    def obtener_temperatura(self) -> float:

        """
        Obtiene la temperatura (en ºC) de la hora indicada

        Args:
            hora (datetime): Hora sobre la que se recoge la temperatura

        Returns:
            float: Temperatura de la hora
        """

        return fc.leer_valor_magnitud("temperatura", "./espacio_inmueble/valores_espacio.json")