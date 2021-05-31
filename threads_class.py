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


# Heredando de la clase Thread a una clase
class ThreadTest(threading.Thread):
    def __init__(self, name, daemon):
        threading.Thread.__init__(self, name=name, daemon=daemon)


    # Sobreescribiendo el metodo padre
    def run(self) -> None:
        logging.info('Iniciando las tareas de la clase!!!')



if __name__ == '__main__':
    thread_class_1 = ThreadTest(name='Thread1Test', daemon=False)
    # .start() => internamente llamara al metodo run
    thread_class_1.start()
