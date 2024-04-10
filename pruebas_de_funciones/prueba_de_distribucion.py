import sys
sys.path.append('/home/serwikk/Domotica/sensores_y_actuadores')

from sensores_y_actuadores import funciones_comunes as fc
from sensores_y_actuadores import sensor_de_temperatura as sensor


def main():
    
    for i in range(0, 1000):
        
        valor = sensor.obtener_temperatura()
        fc.registrar_en_csv('prueba_de_distribucion.csv', ['id', 'temperatura'], {'id': i, 'temperatura': valor})


main()