import requests
import logging
import time
# Modulo para manera los hilos
import threading
from concurrent.futures import ThreadPoolExecutor

# Configuracion inicial del loggin
# filename='./files/logs.txt' // Almacenar los mensajes
# Ejemplos con varios parametros
# %(levelname)s: archivo: %(filename)s mensaje: [%(message)s] fecha_ejecucion: %(asctime)s',
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: | mensaje: [%(message)s] | thread: [%(thread)s] | threadNames: [%(threadName)s] | fecha_ejecucion: [%(asctime)s]',
    datefmt='%d/%m/%y - %H:%M:%S',
    # filename='./files/logs.txt'
)
# Especificando al logger en donde se esta ejecutando __name__ => filename.py
logger = logging.getLogger(__name__)

"""
Usando un pool de threads, permite limitar la cantidad maxima acrear ya que es muy costos para el SO
si se abusa de esto, con el pool si se libera una conexion se pone en uso para crear un nuevo thread
"""


def math_operation(number_1, number_2):
    time.sleep(0.5)
    result = number_1 + number_2

    logging.info(f'Result operation: {result}')


if __name__ == '__main__':
    # max_workers= // establece la cantida maxima de threads disponibles y que se iran libreando
    # thread_name_prefix= // establece un prefijo a los threads name_
     with ThreadPoolExecutor(max_workers=2, thread_name_prefix='group_of_threads') as executor_pool:
        # submit(target, params_target) // permite iniciar la sesion de los threads limitados mediante los pool
        executor_pool.submit(math_operation, 1, 100)
        executor_pool.submit(math_operation, 2, 10)
        executor_pool.submit(math_operation, 100, 200)

        """
        Por consola se puede comprobar como en la 3er ejecucion del pool, se libera la primer posicion y es usada para 
        el thread a ejecutar
        Hasta que no se libere algun thread del pool, quedara a la espera
        """

        # .shutdown() // apaga el pool de threads dentro del contexto, y ya no se pueden usar
        # los que se esten ejecutando no los afecta
        executor_pool.shutdown()