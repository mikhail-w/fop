import sys
from hero import SpaceShip

import pygame


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("OOP")
        self.clock = pygame.time.Clock()
        self.space_surface = pygame.Surface((800, 800))
        self.background = "/home/mikhail/FoP/lesson_10/assets/OuterSpace.png"

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("OOP")
        self.clock = pygame.time.Clock()

    def run(self):
        while True:

            self.screen.blit(self.space_surface, (0, 0))
            self.space_surface.blit(pygame.image.load(self.background), (0, 0))

            # Every time it loops it will check if we decided to exit the game or not
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # <----- WITHIN THIS SPACE WE CAN ADD MORE CODE FOR OUR GAME ---->

            # This method is a form of a refresh, and updates our screen
            pygame.display.update()
            self.clock.tick(60)


my_game = Game()
my_game.run()
