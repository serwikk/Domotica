from espacio_inmueble.controlador import Controlador
from sensores_y_actuadores import sensor_temperatura as st, sensor_humedad as sh, sensor_luz as sl


def main():

    controlador = Controlador("Habitación 1", sensores=[st.SensorTemperatura(), sh.SensorHumedad(), sl.SensorLuz()])
    # controlador.inicializar_valores()
    # print(st.SensorTemperatura().obtener_valor())


if __name__=="__main__":
    main()