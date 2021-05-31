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

# Inicializando el lock, que permitira el bloqueo temporal de un thread
lock_thread = threading.Lock()
# RLock() permite que un thread requeria mas de una vez el mism contexto
# si se ocupa mas de una ves se debe liberar (relase) mas de una vez tambien
# lock_thread = threading.RLock()

WALLET = 0


def deposit():
    global WALLET

    for _ in range(0, 1000000):
        # .acquire() // bloquea temporalmente a solo la ejecucion actual del thread
        lock_thread.acquire()
        WALLET += 1
        # .release() // lobera el thread para que los demas puedan continuar su ejecucion y edicion del mismo espacio en memoria
        lock_thread.release()


def substract():
    global WALLET

    for _ in range(0, 1000000):
        # utilizando el context with
        # hace la misma tarea que acquire y release
        with lock_thread:
            WALLET -= 1




if __name__ == '__main__':
    """
    Race condition
    // Ocurre cuando 2 o mas threads intentan modificar una misma posicion de memoria, puede dar error en el calculo
    
    // La solucion es bloquear la modificacion en memoria para un solo thread y luego liberarlo
    """
    thread1 = threading.Thread(target=deposit)
    thread2 = threading.Thread(target=substract)

    thread1.start()
    thread2.start()

    # Esperando a que ambos threads terminen
    thread1.join()
    thread2.join()

    logging.info(f'The current value of the Wallet is {WALLET}')
