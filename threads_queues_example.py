import random

import requests
import logging
import time
# Modulo para manera los hilos
import threading
import queue

# Configuracion inicial del loggin
# filename='./files/logs.txt' // Almacenar los mensajes
# Ejemplos con varios parametros
# %(levelname)s: archivo: %(filename)s mensaje: [%(message)s] fecha_ejecucion: %(asctime)s',
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: | mensaje: [%(message)s] | thread: [%(thread)s] | proceso: [%(processName)s] | fecha_ejecucion: [%(asctime)s]',
    datefmt='%d/%m/%y - %H:%M:%S',
    # filename='./files/logs.txt'
)
# Especificando al logger en donde se esta ejecutando __name__ => filename.py
logger = logging.getLogger(__name__)

# maxzise // define el limete de capacidad de la cola
queue_main = queue.Queue(maxsize=10)

"""
# Ejercicio

Pusheando y eliminando elementos de la cola, a modo de productor puseha datos y consumer elimina

"""


def producer():
    while True:
        # full() // devuelve True si esta en al stopper definido maxsize
        if not queue_main.full():
            item = random.randint(1, 100)
            queue_main.put(item)

            logging.info(f'Element push {item}')
            random_timer(1, 4)

def consumer():
    while True:
        # .empty() // devuelve True si no es vacia
        if not queue_main.empty():
            # .get() // obtiene el elemento de la cola
            item = queue_main.get()
            # .task_done() // notifica que se puede usar el espacio que ocupaba en la cola
            queue_main.task_done()

            logging.info(f'Element remove {item}')
            random_timer(1, 4)


def random_timer(init_timer, end_timer):
    timer = random.randint(init_timer, end_timer)
    time.sleep(timer)


if __name__ == '__main__':
    thread_producer = threading.Thread(target=producer)
    thread_consumer = threading.Thread(target=consumer)

    thread_producer.start()
    thread_consumer.start()
