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


def get_pokemons_name(response_json):
    name = response_json.get('forms')[0].get('name')
    logging.info(f'El pokemon obtenido es [{name}]')


def error_pokemons():
    logging.error('Error en el request del pokemon')


def generate_request(url, success_callback, error_callback):
    response = requests.get(url)

    if response.status_code == 200:
        success_callback(response.json())
    else:
        error_callback()


if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon/'

    for n_pokemon in range(0, 5):
        thread = threading.Thread(target=generate_request, kwargs={
            'url': url + str(n_pokemon),
            'success_callback': get_pokemons_name,
            'error_callback': error_pokemons
        })
        thread.start()
