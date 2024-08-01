from src.handlers.csv_handler import CSVHandler
from src.handlers.datetime_handler import DatetimeHandler
from src.handlers.pvlib_handler import PVlibHandler
from src.handlers import generation_handler

import logging
from src.handlers.logger_handler import LoggerHandler


def main():

    datetime_handler = DatetimeHandler('2024-08-01 12:00:00')
    print(f"Fecha y hora: {datetime_handler.fecha_completa}")

    # Temperatura
    temperatura_csv_handler = CSVHandler('src/handlers/csv/temperaturas_hora_mes_vitoria.csv')

    valor_temperatura = temperatura_csv_handler.buscar_valor_temperatura(datetime_handler.hora, DatetimeHandler.obtener_mes_string(datetime_handler.mes))

    valor_temperatura = generation_handler.agregar_umbral_a_valor(valor_temperatura)

    print(f"Temperatura: {valor_temperatura}")

    # Humedad
    humedad_csv_handler = CSVHandler('src/handlers/csv/humedad_por_habitaciones.csv')

    valores_espacio = humedad_csv_handler.buscar_valor_humedad('cocina')

    valor_humedad = generation_handler.generar_valor_distribucion_normal(valores_espacio[0], valores_espacio[1])

    print(f"Humedad: {valor_humedad}")

    # LUX # TODO
    datos_solares = PVlibHandler()
    print(datos_solares.obtener_angulo_posicion_solar(datetime_handler))

    # esto devuelve el dataframe de antes. Pero ahora tengo que hacer funciones para obtener los lux dependiendo de estos parámetros 






    



if __name__=="__main__":
    main()