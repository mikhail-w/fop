import pygame


class SpaceShip:

    def __init__(self, image, x, y):
        self._space_ship_surface = pygame.image.load(image)
        self.rect = self._space_ship_surface.get_rect(midbottom=(x, y))

    def get_position(self):
        return (self.rect.x, self.rect.y)

    def draw(self, screen):
        screen.blit(self._space_ship_surface, self._space_ship_rect)
