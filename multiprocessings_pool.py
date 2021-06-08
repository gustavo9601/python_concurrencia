import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
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


def proceso_hijo(numero_hijo, time_to_sleep):
    logging.info(f'Hola desde el proceso hijo #{numero_hijo}')
    time.sleep(time_to_sleep)
    logging.info(f'Fin del proceso hijo #{numero_hijo}')

if __name__ == '__main__':

    # Con el pool se limita la cantidad de procesos simultaneos, y se reutiliza una vez se libere
    with ProcessPoolExecutor(max_workers=2) as executor_pool:
        # .submit(function, params) // return future
        future_1 = executor_pool.submit(proceso_hijo, 1, 5)
        # .add_done_callback // execute function or lambda when the future is end
        future_1.add_done_callback(
            lambda future: logging.info('Callback future 1')
        )

        future_2 = executor_pool.submit(proceso_hijo, 2, 6)
        future_2.add_done_callback(
            lambda future: logging.info('Callback future 2')
        )

