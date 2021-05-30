import requests
import logging
# Modulo para manera los hilos
import threading

# Configuracion inicial del loggin
# filename='./files/logs.txt' // Alamcenar los mensajes
# Ejemplos con varios parametros
# %(levelname)s: archivo: %(filename)s mensaje: [%(message)s] fecha_ejecucion: %(asctime)s',
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: | mensaje: [%(message)s] | thread: [%(thread)s] | proceso: [%(processName)s] | fecha_ejecucion: [%(asctime)s',
    datefmt='%d/%m/%y - %H:%M:%S',
    # filename='./files/logs.txt'
)
# Especificando al logger en donde se esta ejecutando __name__ => filename.py
logger = logging.getLogger(__name__)


def get_name(type):
    url = 'https://randomuser.me/api/'
    response = requests.get(url)
    if response.status_code == 200:

        results = response.json().get('results')
        name = results[0].get('name').get('first')

        print(f"type: [{type}] = name: [{name}]")
    else:
        logger.error('Error en el request')


if __name__ == '__main__':

    # Concurrente
    logger.info('Mediante Thread')
    for _ in range(0, 20):
        # target= // Recibe entidad o funcion a ejecutar de forma concurrente
        # args= // Recibe una lista con los parametros que se necesitaen en el target
        # kwargs= // Recibe en un diccianiro los parametros que necesitan en el target
        thread = threading.Thread(target=get_name, kwargs={'type': 'Concurrente'})
        # Indicamos a python que las instruccion se ejecuten justo en este momento
        thread.start()

    # Secuencial
    logger.info('Forma secuencial')
    for _ in range(0, 20):
        get_name(type='Forma secuencial')
