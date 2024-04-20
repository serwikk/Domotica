from sensores_y_actuadores import sensor_temperatura as st

class Controlador():

    def __init__(self, espacio):
        self.espacio = espacio



def main():
    controlador = Controlador(espacio = "Habitación 1")

    sensor_temperatura1 = st.SensorTemperatura(id = '2324', tipo = 'sensor_temperatura1')

    print(vars(sensor_temperatura1))


if __name__=="__main__":
    main()