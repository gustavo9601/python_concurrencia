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


def countdown(number, multiproccess):
    while number > 0:
        number -= 1
    logging.info(f'multiproccess name {multiproccess}')


if __name__ == '__main__':
    start = time.time()
    count = 10000000
    # target=function to execute
    # args= pass arguments of function
    #kwargs={} params in form of dictioary
    t1 = multiprocessing.Process(target=countdown,
                                 args=(count, 't1'))
    t2 = multiprocessing.Process(target=countdown,
                                 args=(count, 't2'))

    # .join()
    # similar to join rxjs, wait until all the process joined have ended
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    logging.info(f'Tiempo transcurrido {time.time() - start}')
