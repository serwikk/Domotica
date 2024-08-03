from handlers.toml_handler import TOMLHandler
from handlers.logger_handler import LoggerHandler
import logging


loggerHandler = LoggerHandler('pruebas.log', 'pruebas', logging.DEBUG)
config_tomlHandler = TOMLHandler('config.toml', loggerHandler)

print(config_tomlHandler.obtener_valores_seccion('ventanas'))