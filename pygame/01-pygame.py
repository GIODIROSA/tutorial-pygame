import pygame

pygame.init()

width = 800
height = 600

ventana = pygame.display.set_mode((width, height))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()


