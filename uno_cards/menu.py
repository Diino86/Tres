import pygame
import time
# importing from local .py files
from button import *
from display import *
from menu2 import *


class menu1(menu_display):
    def __init__(self):
        menu_display.__init__(self)
        
        # Button images
        self.tres_logo_img = img('tres_logo')
        self.start_img = img('start_button')
        self.quit_img = img('quit_button')

        # Button(x, y, image, scale)
        self.tres_logo = Button(350, 40, self.tres_logo_img.image, 0.8)
        self.start_button = Button(276, 420, self.start_img.image, 0.45)
        self.quit_button = Button(703, 420, self.quit_img.image, 0.45)
    
    # Loop reads window by 60 FPS, quits when window closed
    def main(self):
        while self.RUNNING:
            # 60 fps
            self.clock.tick(self.FPS)
            
            # Show background and images
            self.screen.fill(self.ORANGE)
            self.tres_logo.draw_only(self.screen)
            
            # Button interaction
            if self.start_button.draw(self.screen) == True:
                time.sleep(0.1)
                m2 = menu2()
                m2.main()
            if self.quit_button.draw(self.screen) == True:
                self.RUNNING = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False
                    
            pygame.display.update()
            
        pygame.quit()

