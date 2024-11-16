import pygame
import constantes

pygame.init()

ventana = pygame.display.set_mode((constantes.WIDTH_WINDOWS, constantes.HEIGHT_WINDOWS))
pygame.display.set_caption("Consumo electrico")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()


