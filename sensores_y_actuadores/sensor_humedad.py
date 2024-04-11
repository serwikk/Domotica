import funciones_comunes as fc
import random as rd


(humedad_min_normal, 
humedad_max_normal, 
humedad_media_dist_normal,
humedad_desviacion_estandar, 
humedad_outlier_activados) = fc.obtener_valores_config('sensor_humedad')

def obtener_humedad():

    # Si los outliers están activados y con un 5% de probabilidad
    # if temperatura_outlier_activados and rd.random() < 0.05:

    #     outlier = fc.generar_outlier(temperatura_min_outlier, temperatura_max_outlier)

    #     return round(outlier, 2)
        
        
    # En caso contrario:
    humedad = fc.generar_valor_distribucion_normal( media_dist_normal = humedad_media_dist_normal, 
                                                        desviacion_estandar = humedad_desviacion_estandar, 
                                                        min_temp = humedad_min_normal, 
                                                        max_temp = humedad_max_normal)
    
    
    return round(humedad, 2)

def main():
    
    valor = obtener_humedad()

    return valor




if __name__ == "__main__":
    main()