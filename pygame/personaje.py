import pygame
import constantes


class Personaje():
    def __init__(self, x, y, animaciones):
        self.flip = False
        self.animaciones = animaciones
        #imagen de la animacion que se esta mostrando actualmente
        self.frame_index = 0
        # aquí se almacena la hora actual (en milisegundos desde que se inició 'pygame')
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        self.shape = pygame.Rect(0,0, constantes.WIDTH_PERSONAJE, constantes.HEIGHT_PERSONAJE)
        self.shape.center = (x,y)

    def update(self):
        cooldown_animacion = 100
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0

    def draw(self, interface):
        image_flip = pygame.transform.flip(self.image, self.flip, False)
        interface.blit(image_flip, self.shape)
        #pygame.draw.rect(interface, constantes.COLOR_PERSONAJE, self.shape, width= 1)

    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False


        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y


