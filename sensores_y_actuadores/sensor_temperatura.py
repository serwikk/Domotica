
# from config import TEMPERATURA_MIN, TEMPERATURA_MAX, HOY



class SensorTemperatura():

    def __init__(self, id, tipo, en_funcionamiento = True, unidad='c'):
        self.id = id
        self.tipo = tipo
        self.en_funcionamiento = en_funcionamiento
        self.unidad = unidad

    def obtener_temperatura(self, hora) -> float:

        """
        Obtiene la temperatura (en ºC) de la hora indicada

        Args:
            hora (datetime): Hora sobre la que se recoge la temperatura

        Returns:
            float: Temperatura de la hora
        """

        return fc.generar_valor_ciclico(fc.hora_datetime_a_float(hora), TEMPERATURA_MIN, TEMPERATURA_MAX)