import funciones_comunes as fc
from config import HUMEDAD_MIN, HUMEDAD_MAX

def obtener_humedad():

    return fc.generar_valor_distribucion_normal(HUMEDAD_MIN, HUMEDAD_MAX)

def main():
    
    valor = obtener_humedad()
    
    return valor




if __name__ == "__main__":
    main()