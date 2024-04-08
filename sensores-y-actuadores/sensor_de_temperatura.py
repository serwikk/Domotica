import funciones_comunes as fc
import random as rd
from time import sleep

temperatura_min_normal = 18
temperatura_max_normal = 23
temperatura_min_outlier = 14
temperatura_max_outlier = 28
temperatura_probabilidad_outlier = 0.05
temperatura_media_dist_normal = 20
temperatura_desviacion_estandar = 1
temperatura_outlier_activados = True



def obtener_temperatura():

    # Si los outliers están activados y con un 5% de probabilidad
    if temperatura_outlier_activados and rd.random() < 0.05:

        outlier = fc.generar_outlier(temperatura_min_outlier, temperatura_max_outlier)

        return round(outlier, 2)
        
        
    # En caso contrario:
    temperatura = fc.generar_valor_distribucion_normal( media_dist_normal = temperatura_media_dist_normal, 
                                                        desviacion_estandar = temperatura_desviacion_estandar, 
                                                        min_temp = temperatura_min_normal, 
                                                        max_temp = temperatura_max_normal)
    
    
    return round(temperatura, 2)





def main():
    
    valor = obtener_temperatura()

        


if __name__ == "__main__":
    main()