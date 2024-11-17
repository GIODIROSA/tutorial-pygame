import pygame
import constantes
from personaje import Personaje
pygame.init()

jugador = Personaje(50, 50)



ventana = pygame.display.set_mode((constantes.WIDTH_WINDOWS, constantes.HEIGHT_WINDOWS))
pygame.display.set_caption("Consumo electrico")

#definir variables de movimiento del jugador
mover_arriba= False
mover_abajo= False
mover_izquierda= False
mover_derecha= False

# Controlar el frame rate
reloj = pygame.time.Clock()


run = True
while run:

    # Vaya a 60 fps
    reloj.tick(constantes.FPS)

    # Pintar fondo mientras se mueve
    ventana.fill(constantes.COLOR_BG)

    #Calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD

    # Metodo Movimiento
    jugador.movimiento(delta_x, delta_y)

    # Metodo dibujar personaje
    jugador.draw(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

        # Para cuando se suelta la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False



    pygame.display.update()
pygame.quit()



