import requests
import logging
import time
# Modulo para manera los hilos
import threading

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


def thread_1(event):
    logging.info('Ejecutando thread_1')
    # .wait() // detendra la ejecucion hasta que la señal sea seteada en el evento
    event.wait()
    logging.info('Ejecutando thread_1 Terminada')


def thread_2(event):
    logging.info('Ejecutando thread_2')

    # .is_set() // verifica si la señal fue seteada en el evento
    while not event.is_set():
        logging.info('Ejecutando thread_2 a la espera de la señal')
        time.sleep(0.5)


if __name__ == '__main__':

    """
    Creando el evento
    // Util hasta que no termine cierta actividad no emita o cambie el estado de la bandera
    """
    event = threading.Event()

    thread_1 = threading.Thread(target=thread_1, args=(event,))
    thread_2 = threading.Thread(target=thread_2, args=(event,))

    thread_1.start()
    thread_2.start()

    time.sleep(3)

    # Flag / True or False // señal de los eventos , empiezan por false
    # Cambia el estado de la señal
    event.set()


    # Si se requiere limpiar el estado del evento
    # event.clear()