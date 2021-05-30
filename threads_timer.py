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


def callback_test():
    logging.info('Hola se ejecuto el calback')

if __name__ == '__main__':
    # Con timer se pasa la cantidad de segundos a ejecutar la funcion pasada como parametro "calback"
    thread = threading.Timer(3, callback_test)
    thread.start()

    logger.info('A la espera del callback')
