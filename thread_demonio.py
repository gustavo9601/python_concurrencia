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

def thread_1():
    logging.info('Iniciando thread 1')
    time.sleep(2)
    logging.info('Finalizando thread 1')


def daemon_thread():
    count = 1
    while True:
        logging.info(f'Ejecutandose daemon #{count}')
        time.sleep(0.5)
        count += 1

if __name__ == '__main__':
    # daemon=True
    # Especificando que es de tipo daemon, se invierte la lofica del thread
    # El thread se desacopla del thread principal y no se finalizara hasta cuando finalice todo el script
    thread1 = threading.Thread(target=daemon_thread, daemon=True)

    thread1.start()

    logging.info('Final del programa')
    input('Presiona una tecla para finalizar el daemon')