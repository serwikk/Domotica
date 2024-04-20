from simuladores import funciones_comunes as fc

from sensores_y_actuadores.sensor import Sensor

class SensorHumedad(Sensor):

    def __init__(self, en_funcionamiento=True, unidad= "%"):
        
        super().__init__( id= fc.generar_id_aleatorio("hum-"), magnitud = "humedad", en_funcionamiento = en_funcionamiento, unidad = unidad)

    def obtener_valor(self):

        return fc.leer_valor_magnitud("humedad", "./espacio_inmueble/valores_espacio.json")
