import pygame

class img:
    def __init__(self, image):
        self.image = pygame.image.load('button_img/' + image).convert_alpha()

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

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