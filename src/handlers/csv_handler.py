import csv
import logging
from src.handlers.logger_handler import LoggerHandler

class CSVHandler:

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.delimiter = ','
        self.valores = self.cargar_csv()
        self.logger_handler = LoggerHandler('/home/serwikk/Domotica/logs/csv_handler.log', logging.INFO)


    def cargar_csv(self):
        """
        Devuelve todos los datos como un diccionario
        """

        with open(self.ruta_archivo, 'r', newline='') as archivo:

            datos = []
            
            reader = csv.DictReader(archivo, delimiter=self.delimiter)

            for row in reader:

                datos.append(row)

            return datos
    

    def guardar_csv(self):
        """
        Guarda los valores actuales en el archivo CSV
        """

        with open(self.ruta_archivo, 'w') as archivo:
            csv.writer(self.valores, archivo, delimiter=self.delimiter)


    def buscar_valor_celda(self, hora, mes):

        for fila in self.valores:

            if fila['hora'] == str(hora):

                try:

                    valor_celda = fila[mes]
                
                    self.logger_handler.logger.info(f"Obtenido el valor {valor_celda} de la hora {hora} del mes de {mes}")

                    return float(valor_celda)
                
                except Exception as e:
                    
                    self.logger_handler.logger.error(e)

            