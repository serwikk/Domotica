import pvlib
from pvlib.location import Location
import pandas as pd
from src.handlers.datetime_handler import DatetimeHandler
from src.handlers.csv_handler import CSVHandler

class PVlibHandler:

    def __init__(self, latitud=42.84419, longitud=-2.68602, timezone = 'Europe/Madrid') -> None:
        self.latitud = latitud
        self.longitud = longitud
        self.timezone = timezone


    def obtener_valores_posicion_solar_dia_completo(self, dia: str, intervalo: int = 10):

        
        csv_handler = CSVHandler(ruta_archivo=f'resultados/posicion_solar/{DatetimeHandler.fecha_cambiar_formato_fecha(dia)}.csv', 
                                 encabezados=['Hora','Apparent Zenith','Zenith','Apparent Elevation','Elevation','Azimuth','Equation of time'], 
                                 delimiter=';')

        for hora in range(0, 24, 1):

            for minuto in range(0, 60, intervalo):

                datetime_handler = DatetimeHandler(f'{dia} {hora}:{minuto}:00')
                
                location = Location(self.latitud, self.longitud, self.timezone)

                time = pd.Timestamp(datetime_handler.fecha_completa, tz=self.timezone)

                solar_position = location.get_solarposition(time)

                csv_handler.guardar_nuevo_valor(solar_position.to_csv())  # TODO terminar esto no funciona
                  

                break # TODO eliminar
        
            break # TODO eliminar


    def obtener_valor_posicion_solar_actual(self, fecha):
                    

            datetime_handler = DatetimeHandler(f'{fecha.anyo}-{fecha.mes}-{fecha.dia} {fecha.hora}:{fecha.minuto}:{fecha.segundo}')
                
            location = Location(self.latitud, self.longitud, self.timezone)

            time = pd.Timestamp(datetime_handler.fecha_completa, tz=self.timezone)

            solar_position = location.get_solarposition(time)

            return solar_position
                

if __name__=="__main__":

    pvlib_handler = PVlibHandler()

    pvlib_handler.obtener_valores_posicion_solar_dia_completo('2024-06-21')