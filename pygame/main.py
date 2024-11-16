import pygame
import constantes
from personaje import Personaje

jugador = Personaje(50, 50)

pygame.init()

ventana = pygame.display.set_mode((constantes.WIDTH_WINDOWS, constantes.HEIGHT_WINDOWS))
pygame.display.set_caption("Consumo electrico")

run = True
while run:

    jugador.draw(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()



