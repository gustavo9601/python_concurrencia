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


def deposit(namespace, lock):
    for _ in range(1, 10000):
        # al igual que en threads convencionales
        # toma la variable y bloquea su edidicion hasta que sea liberada con release
        lock.acquire()
        namespace.balance += 1
        lock.release()

def withdraw(namespace, lock):
    for _ in range(1, 10000):
        # Al igual que en los threads convencionales
        # se puede usar lock en un contexto el cual se encargara de adquirirlo y liberarlo
        with lock:
            namespace.balance -= 1


if __name__ == '__main__':
    # Inicializando el manager
    manager = multiprocessing.Manager()
    # Inicializa el espacio en memoria para crear variables y poder compartir entre procesos
    namespace = manager.Namespace()
    # Una vez definido el namespace, a modo de diccionario u objeto se pueden añadir nuevas variables
    namespace.balance = 0
    # El lock permitira evitar el race condition cuando se este modificando una misma variable compartida
    lock = manager.Lock()

    proccess_1 = multiprocessing.Process(target=deposit, args=(namespace,lock))
    proccess_2 = multiprocessing.Process(target=withdraw, args=(namespace,lock))

    proccess_1.start()
    proccess_2.start()

    proccess_1.join()
    proccess_2.join()

    logging.info(f'El balance final es de {namespace.balance}')