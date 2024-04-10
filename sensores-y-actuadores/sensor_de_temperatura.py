import funciones_comunes as fc
import random as rd


(temperatura_min_normal, 
temperatura_max_normal, 
temperatura_min_outlier, 
temperatura_max_outlier,
temperatura_probabilidad_outlier,
temperatura_media_dist_normal,
temperatura_desviacion_estandar, 
temperatura_outlier_activados) = fc.obtener_valores_config('sensor_temperatura')

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

    print(valor)

        


if __name__ == "__main__":
    main()