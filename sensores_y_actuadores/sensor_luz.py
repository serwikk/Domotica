from simuladores import funciones_comunes as fc

from sensores_y_actuadores.sensor import Sensor

class SensorLuz(Sensor):

    def __init__(self, en_funcionamiento=True, unidad= "lm"):
        
        super().__init__( id= fc.generar_id_aleatorio("lux-"), magnitud = "luz", en_funcionamiento = en_funcionamiento, unidad = unidad)

    def obtener_luz(self):

        return fc.leer_valor_magnitud("luz", "./espacio_inmueble/valores_espacio.json")