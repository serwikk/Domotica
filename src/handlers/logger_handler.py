import logging

class LoggerHandler:

    def __init__(self, nombre_archivo, nivel):
        self.nombre_archivo = nombre_archivo
        self.nivel = nivel
        
        # Crear un logger para esta instancia de LoggerHandler
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.nivel)
        
        # Crear un manejador de archivo
        file_handler = logging.FileHandler(self.nombre_archivo)
        file_handler.setLevel(self.nivel)
        
        # Definir el formato del log
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        # Agregar el manejador al logger
        self.logger.addHandler(file_handler)