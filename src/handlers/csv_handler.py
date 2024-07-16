import csv
import logging

class CSVHandler:

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.delimiter = ','
        self.valores = self.cargar_csv()


    def cargar_csv(self):
        """
        Devuelve todos los datos como un diccionario
        """

        with open(self.ruta_archivo, 'r', newline='') as archivo:

            datos = []
            
            reader = csv.reader(archivo, delimiter=self.delimiter)

            for row in reader:

                datos.append(row)

            return datos
    

    def guardar_csv(self):
        """
        Guarda los valores actuales en el archivo CSV
        """

        with open(self.ruta_archivo, 'w') as archivo:
            csv.writer(self.valores, archivo, delimiter=self.delimiter)


