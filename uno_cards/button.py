import pygame
import time

class img:
    def __init__(self, image):
        self.image = pygame.image.load(f'button_img/{image}.png').convert_alpha()

# class card:
#     def __init__(self, number, color):
#         self.number = number
#         self.color = color
#         self.image = pygame.image.load(f'uno_card_img/uno_card-{str(self.color)}{str(self.number)}.png').convert_alpha()

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw_only(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    def draw(self, surface):
        action = False
        
        #mouse position
        pos = pygame.mouse.get_pos()
        
        #check mouseover and clicked condition
        #if left click[0] is clicked[1] and self.clicked still Flase
        #then turn self.clicked = True
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
        #if left click[0] is no longer clicked[0]
        #then turn self.clicked = False
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        return action

#Version2_________________________________________________________________

class card:
    def __init__(self, number, color):
        self.scale = 0.25
        self.number = number
        self.color = color
        self.load_image = pygame.image.load(f'uno_card_img/uno_card-{str(self.color)}{str(self.number)}.png').convert_alpha()
        
        width = self.load_image.get_width()
        height = self.load_image.get_height()
        self.image = pygame.transform.scale(self.load_image, (int(width * self.scale), int(height * self.scale)))
        self.rect = self.image.get_rect()
        self.clicked = False
        
    def draw(self, x, y, surface):
        action = False
        self.rect.topleft = (x, y)
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                time.sleep(0.2)
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        surface.blit(self.image, (x, y))
        
        return action