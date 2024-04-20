from simuladores import funciones_comunes as fc


class Sensor:

    def __init__(self, id, magnitud, en_funcionamiento, unidad):
        self.id = id
        self.magnitud = magnitud
        self.en_funcionamiento = en_funcionamiento
        self.unidad = unidad


    def obtener_valor(self) -> float: 
        """
        Obtiene el valor del sensor

        Returns:
            float: Temperatura de la hora
        """

        
        return fc.leer_valor_magnitud(self.magnitud, "./espacio_inmueble/valores_espacio.json")