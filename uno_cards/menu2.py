import pygame
from button import *
from menu import menu_display

class menu2(menu_display):
    def __init__(self):
        menu_display.__init__(self)
        
        
        self.two_players_img = img('2-players_button.png')
        self.two_players_button = Button(450, 250, self.two_players_img.image, 0.45)
        
    def main(self):
        while self.RUNNING:
            self.clock.tick(self.FPS)
            self.screen.fill(self.ORANGE)
            
            if self.two_players_button.draw(self.screen) == True:
                pass
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False
                    
            pygame.display.update()
            
        pygame.quit()
