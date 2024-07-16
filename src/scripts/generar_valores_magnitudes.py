from src.handlers.csv_handler import CSVHandler


def main():
    
    csv_handler = CSVHandler('/home/serwikk/Domotica/src/handlers/csv/temperaturas_hora_mes_vitoria.csv')

    print(csv_handler.valores)

    pass

if __name__=="__main__":
    main()