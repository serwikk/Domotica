import json


def obtener_datos():

    with open("casa_ejemplo.json", "r") as file:

        return json.load(file)




if __name__=="__main__":

    datos = obtener_datos()
    print(datos)


    