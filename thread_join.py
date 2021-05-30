import time
import requests
import logging
# Modulo para manera los hilos
import threading

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: | mensaje: [%(message)s] | thread: [%(thread)s] | proceso: [%(processName)s] | fecha_ejecucion: [%(asctime)s]',
    datefmt='%d/%m/%y - %H:%M:%S',
    # filename='./files/logs.txt'
)
# Especificando al logger en donde se esta ejecutando __name__ => filename.py
logger = logging.getLogger(__name__)

"""
join() Similar a operador jpin rxjs
// Eejecuta los threads pero hasta que  se completen ambos no retorna el resultado
"""


def conexion_bd():
    logging.info('Comenzando la conexion de la BD')
    time.sleep(2)
    logging.info('Termino la conexion de la BD')

def consulta_web():
    logging.info('Comenzando consulta en la web')
    time.sleep(3)
    logging.info('Termino consulta en la web')



if __name__ == '__main__':
    thread1 = threading.Thread(target=conexion_bd)
    thread2 = threading.Thread(target=consulta_web)

    thread1.start()
    thread2.start()
    # .join() indica al thread principal que debe esperar los threads en mencion para continuar la ejecucion del script
    thread1.join()
    thread2.join()

    logging.info('Final del programa')
