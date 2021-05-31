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

USER = dict()


def get_info_user(url, event):
    global USER
    response = requests.get(url)
    if response.status_code == 200:
        USER = response.json().get('results')[0]
        logging.info('Seteando el evento')
        event.set()


def show_user_name(event):
    logging.info('Esperando la seteada del evento')
    event.wait()

    name = USER.get('name').get('first')
    logging.info(f'El nombre obtenido y a mostrar es {name}')


if __name__ == '__main__':
    """
    Creando el evento
    // Util hasta que no termine cierta actividad no emita o cambie el estado de la bandera
    """
    event = threading.Event()

    thread_1 = threading.Thread(target=get_info_user, args=('https://randomuser.me/api/', event))
    thread_2 = threading.Thread(target=show_user_name, args=(event,))

    thread_1.start()
    thread_2.start()
