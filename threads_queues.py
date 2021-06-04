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

def show_ements():

    # Retornara true si se encuentra vacia
    while not queue_1.empty():
        item = queue_1.get()

        logging.info(f'El elemento es {item}')

        # Indicando al thread que debe librerar la cola que ocupaba para que otro pueda utilizarlo
        queue_1.task_done()

        time.sleep(0.5)

if __name__ == '__main__':
    # // First In First Out (FIFO)
    queue_1 = queue.Queue()

    for val in range(1, 20):
        # Pusheando valor a la cola
       queue_1.put(val)

    for _ in range(4):
        thread = threading.Thread(target=show_ements)
        thread.start()