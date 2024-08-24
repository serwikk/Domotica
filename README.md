# Datos generales
**Repositorio**: Domótica  
**Proyecto**: CARE (Centralized Automation for Residential Efficiency) - Personalización Inteligente para una Experiencia Eficiente en Hogares Automatizados

# Descripción
Este repositorio contiene la preparación e invocación de contenedores y volúmenes *docker* para la centralización de los datos enviados desde el repositorio **Domotica_Controller**, entre otros.

## Contenido del docker

- **Elasticsearch**:
    - Versión: 8.15.0
    - Puerto: 9200
- **Kibana**:
    - Versión: 8.15.0
    - Puerto: 5601


# Instalación

## 1. Clonar el repositorio
```git clone https://github.com/serwikk/Domotica.git```  
```cd Domotica```

## 2. Instalación de docker en WSL
https://learn.microsoft.com/es-es/windows/wsl/tutorials/wsl-containers

# Uso

## Iniciar el contenedor
``` bash scripts/iniciar_docker.sh```

## Detener el contenedor
``` bash scripts/detener_docker.sh```