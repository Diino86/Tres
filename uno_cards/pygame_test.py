import pygame
import button

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tres: Fun with the family')

# Load button images
tres_logo = pygame.image.load('tres_logo.png').convert_alpha()
start_img = pygame.image.load('start_button.png').convert_alpha()
quit_img = pygame.image.load('quit_button.png').convert_alpha()

ORANGE = (232, 115, 26)
FPS = 60


# Button class



tres_logo = button.Button(370, 40, tres_logo, 0.8)
start_button = button.Button(276.6, 420, start_img, 0.45)
quit_button = button.Button(703.3, 420, quit_img, 0.45)


# Window color (RGB)
def draw_window():
    screen.fill(ORANGE)
    
    tres_logo.draw(screen)
    

# Loop reads window by 60 FPS, quits when window closed
def main():
    clock = pygame.time.Clock()
    
    run = True
    while run:
        #60 fps
        clock.tick(FPS)
        
        #Show background and images
        draw_window()
        
        if start_button.draw(screen) == True:
            print('Start')
        if quit_button.draw(screen) == True:
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        pygame.display.update()
        
    pygame.quit()


# Game only starts when this file executes
if __name__ == "__main__":
    main()
