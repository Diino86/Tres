import pygame

class menu_display:
    def __init__(self):
        # Window size and title
        self.WIDTH, self.HEIGHT = 1280, 720
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Tres: Fun with the family')
        self.RUNNING = True
        self.clock = pygame.time.Clock()
        self.ORANGE = (232, 115, 26)
        self.FPS = 60