import pygame
import time
from button import *
from display import *
# Change 'test' later
from test import *


class menu2(menu_display):
    def __init__(self):
        menu_display.__init__(self)
        self.menu2_RUNNING = True
        
        self.two_players_img = img('2-players_button')
        self.back_img = img('back_button')
        
        self.two_players_button = Button(450, 250, self.two_players_img.image, 0.45)
        self.back_button = Button(1000, 50, self.back_img.image, 0.45)
        
    def main(self):
        while self.menu2_RUNNING:
            self.clock.tick(self.FPS)
            self.screen.fill(self.ORANGE)
            
            if self.two_players_button.draw(self.screen) == True:
                time.sleep(0.1)
                game = game_menu()
                game.main()
            if self.back_button.draw(self.screen) == True:
                self.menu2_RUNNING = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu2_RUNNING = False
                    
            pygame.display.update()

