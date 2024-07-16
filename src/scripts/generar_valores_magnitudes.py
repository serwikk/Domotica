from src.handlers.csv_handler import CSVHandler
from src.handlers.datetime_handler import DatetimeHandler
from src.handlers import generation_handler


def main():

    datetime_handler = DatetimeHandler()
    csv_handler = CSVHandler('/home/serwikk/Domotica/src/handlers/csv/temperaturas_hora_mes_vitoria.csv')

    valor_temperatura = csv_handler.buscar_valor_celda(datetime_handler.hora, datetime_handler.obtener_mes_string())

    valor_final = generation_handler.agregar_umbral_a_valor(valor_temperatura)

    print(valor_final)

    



if __name__=="__main__":
    main()