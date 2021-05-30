import time

import requests
import logging
# Modulo para manera los hilos
import threading
from concurrent.futures import Future

"""
Los futures
Permite ejecutar N cantidad de callbacks una vez se les asigne un valor
// Similar a una Promesa en un JS
"""


logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: | mensaje: [%(message)s] | thread: [%(thread)s] | proceso: [%(processName)s] | fecha_ejecucion: [%(asctime)s]',
    datefmt='%d/%m/%y - %H:%M:%S',
    # filename='./files/logs.txt'
)
# Especificando al logger en donde se esta ejecutando __name__ => filename.py
logger = logging.getLogger(__name__)


def callback_future(future):
    logging.info(f"Resultado del llamado a callback_future {future.result()}")


if __name__ == '__main__':
    future1 = Future()
    future1.add_done_callback(callback_future)
    future1.add_done_callback(
        lambda future : logging.info('Ejecutando la lambda')
    )


    logging.info('Inicio de la tarea')
    time.sleep(2)
    logging.info('Termino la dormidera')
    logging.info('Asignando valor al future')
    future1.set_result('Artificial Intelligence by GM')

    # future1.done()
    # Es true en cuanto se le setee un valor al future
    while not future1.done():
        print("Esperando un valor al future")
    else:
        print("Termino la espera !!!!")