import toml
from logger_handler import LoggerHandler
import logging

class TOMLHandler:

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.valores = self.cargar_toml()


    def cargar_toml(self) -> dict:
        """
        Devuelve todos los datos como un diccionario
        """

        with open(self.ruta_archivo, 'r') as archivo:
            return toml.load(archivo)
    

    def guardar_toml(self):
        """
        Guarda los valores actuales en el archivo TOML
        """

        with open(self.ruta_archivo, 'w') as archivo:
            toml.dump(self.valores, archivo)


    def obtener_valores_seccion(self, seccion) -> dict:
        """
        Devuelve todos los valores de una sección
        """

        return self.valores[seccion]     
    

    def obtener_valor(self, seccion, clave):
        """
        Devuelve el valor de la sección y clave especificadas 
        """

        try:
            return self.valores[seccion][clave]
        
        except KeyError:
            msg = 'Sección o clave no encontrada'
            loggerHandler.logger.error(msg)
            return None
        
    
    def establecer_valor(self, seccion, clave, valor):
        """
        Establece un valor específico en una sección y clave del archivo TOML
        """

        if seccion not in self.valores:
            self.valores[seccion] = {}
            loggerHandler.logger.info(f'Sección "{seccion}" creada')
        
        self.valores[seccion][clave] = valor
        self.guardar_toml()
        loggerHandler.logger.info(f'Clave "{clave}" actualizada en la sección "{seccion}" con el valor: {valor} ({type(valor)})')



if __name__ == "__main__":
    TOMLhandler = TOMLHandler(ruta_archivo="src/info_casa/datos_actuales.toml")

    loggerHandler = LoggerHandler('debug.log', logging.DEBUG)
