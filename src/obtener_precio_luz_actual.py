import requests
from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
import pytz



def obtener_precio_luz_actual():

    URL = "https://api.preciodelaluz.org"

    endpoint = "/v1/prices/now?zone=PCB"

    URL_completa = URL + endpoint

    respuesta = requests.get(URL_completa)

    if respuesta.status_code == 200:
        data = respuesta.json()

        return data

    else:
        print(f"Error en la petición: {respuesta.status_code}")


def transformar_datos(data):

    datos_finales = dict()

    hora = data['hour'].split("-")[0]

    fecha = datetime.strptime(f"{data['date']} {hora}", "%d-%m-%Y %H")
    
    huso = "Europe/Madrid"

    timezone = pytz.timezone(huso)

    spain_time = datetime.now(timezone)

    is_dist = spain_time.dst() != timedelta(0)

    if is_dist:
        fecha -= timedelta(hours=2)

    else:
        fecha -= timedelta(hours=1)

    datos_finales['fecha'] = fecha.strftime("%Y-%m-%dT%H:00:00")

    datos_finales['es_barato'] = data['is-cheap']
    datos_finales['por_debajo_de_media'] = data['is-under-avg']
    datos_finales['precio'] = data['price'] / 1000
    datos_finales['unidades'] = "€/kWh"

    return datos_finales



def main():

    data = obtener_precio_luz_actual()

    if not data:
        return
    
    
    es = Elasticsearch("http://localhost:9200")
    
    if not es.ping():
        return
    
    datos_finales = transformar_datos(data)

    es.index(index="precio_luz", document=datos_finales)


if __name__ == "__main__":
    main()