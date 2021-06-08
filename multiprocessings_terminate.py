import time
import multiprocessing
import logging

# Configuracion inicial del loggin
# filename='./files/logs.txt' // Almacenar los mensajes
# Ejemplos con varios parametros
# %(levelname)s: archivo: %(filename)s mensaje: [%(message)s] fecha_ejecucion: %(asctime)s',
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: | mensaje: [%(message)s] | thread: [%(thread)s] | proceso: [%(processName)s] | PID: [%(process)s] | fecha_ejecucion: [%(asctime)s]',
    datefmt='%d/%m/%y - %H:%M:%S',
    # filename='./files/logs.txt'
)
# Especificando al logger en donde se esta ejecutando __name__ => filename.py
logger = logging.getLogger(__name__)


def proceso_hijo():
    logging.info('Hola desde el proceso hijo')
    time.sleep(20)
    logging.info('Fin del proceso hijo')

if __name__ == '__main__':
    process_1 = multiprocessing.Process(target=proceso_hijo)
    process_1.start()

    time.sleep(2)

    # .is_alive() // return boolean if already now is executing
    if process_1.is_alive():
        # .terminate() // force the end of the process
        process_1.terminate()
        logging.info('Proceso hijo finalizado a la fuerza')

    logging.info('Fin del programa')
