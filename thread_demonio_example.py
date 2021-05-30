import sys
import time
import requests
import logging
# Modulo para manera los hilos
import threading
# Libreria de graficos
import pygame

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: | mensaje: [%(message)s] | thread: [%(thread)s] | proceso: [%(processName)s] | fecha_ejecucion: [%(asctime)s]',
    datefmt='%d/%m/%y - %H:%M:%S',
    # filename='./files/logs.txt'
)
# Especificando al logger en donde se esta ejecutando __name__ => filename.py
logger = logging.getLogger(__name__)

# Init pygame settings
pygame.init()
width = 600
height = 600
TEXT_BTC = '1.0'

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Texto')

white = (255, 255, 255)
red = (115, 38, 80)
black = (0, 0, 0)

font = pygame.font.Font('./fonts/Roboto-Thin.ttf', 24)


def get_btc_price(url='https://api.bitso.com/v3/ticker'):
    global TEXT_BTC

    while True:
        response = requests.get(url)
        if response.status_code == 200:
            payload = response.json().get('payload')[0]
            price = payload.get('last')
            logger.info(f'Price got {price}')
            TEXT_BTC = f'BTC: {price} MXN'

            time.sleep(1)


if __name__ == '__main__':
    # daemon=True
    # Especificando que es de tipo daemon, se invierte la lofica del thread
    # El thread se desacopla del thread principal y no se finalizara hasta cuando finalice todo el script
    thread = threading.Thread(target=get_btc_price, daemon=True)
    thread.start()

    # Ejecutando el display pygame
    while True:
        text = font.render(TEXT_BTC, True, black)
        rect = text.get_rect()
        rect.center = (width // 2, height // 2)
        surface.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        surface.blit(text, rect)

        pygame.display.update()
