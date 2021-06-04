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

URLS = [
    'https://gmail.com/',
    'https://eybooks.to/',
    'https://platzi.com/datos/',
    'https://platzi.com/ai/',
    'https://www.digitalocean.com/community/tutorials/crear-un-nuevo-usuario-y-otorgarle-permisos-en-mysql-es'
]

URLS_2 = [
    'https://www.linuxito.com/seguridad/612-listar-todos-los-usuarios-que-tienen-acceso-a-una-base-de-datos-en-mysql',
    'https://www.redvirtual.bid/',
    'https://descargasnsn.to/'
]


def generate_request(url):
    return requests.get(url).status_code


def check_status_code(future_thread, code=None):
    if code:
        response_code = code
    else:
        response_code = future_thread.result()

    logging.info(f'Codigo status url form future: {response_code}')


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2, thread_name_prefix='urls_thread') as executor_pool:
        for url in URLS:
            # Inicianlizando el thread para que use la conexion del pool disponible
            future_thread = executor_pool.submit(generate_request, url)
            # Añadiendo un callback enviando el futuro del thread obtenido
            future_thread.add_done_callback(check_status_code)

            # Usando map()
            # permitira ejecutar la funcion como primer parametro al iterador como segundo parametro, pero de forma concurrente
            results_map_pool_urls = executor_pool.map(generate_request, URLS_2)  # retorna un yield (generador)
            for result_url in results_map_pool_urls:
                check_status_code(None, result_url)
