import pygame
import constantes


class Personaje():
    def __init__(self, x, y):
        self.shape = pygame.Rect(0,0, constantes.WIDTH_PERSONAJE, constantes.HEIGHT_PERSONAJE)
        self.shape.center = (x,y)

    def draw(self, interface):
        pygame.draw.rect(interface, constantes.COLOR_PERSONAJE, self.shape)

    def movimiento(self, delta_x, delta_y):
        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y


