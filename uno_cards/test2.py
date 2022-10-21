import pygame
import button


WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tres: Fun with the family')
ORANGE = (232, 115, 26)
FPS = 60


CardBack = pygame.image.load('uno_card_img/uno_card-back.png').convert_alpha()

Red0a = pygame.image.load('uno_card_img/uno_card-red0.png').convert_alpha()
Red1a = pygame.image.load('uno_card_img/uno_card-red1.png').convert_alpha()
Red2a = pygame.image.load('uno_card_img/uno_card-red2.png').convert_alpha()
Red3a = pygame.image.load('uno_card_img/uno_card-red3.png').convert_alpha()
Red4a = pygame.image.load('uno_card_img/uno_card-red4.png').convert_alpha()
Red5a = pygame.image.load('uno_card_img/uno_card-red5.png').convert_alpha()
Red6a = pygame.image.load('uno_card_img/uno_card-red6.png').convert_alpha()
Red7a = pygame.image.load('uno_card_img/uno_card-red7.png').convert_alpha()
Red8a = pygame.image.load('uno_card_img/uno_card-red8.png').convert_alpha()
Red9a = pygame.image.load('uno_card_img/uno_card-red9.png').convert_alpha()
RedDraw2a = pygame.image.load('uno_card_img/uno_card-reddraw2.png').convert_alpha()
RedReversea = pygame.image.load('uno_card_img/uno_card-redreverse.png').convert_alpha()
RedSkipa = pygame.image.load('uno_card_img/uno_card-redskip.png').convert_alpha()

Red1b = pygame.image.load('uno_card_img/uno_card-red1.png').convert_alpha()
Red2b = pygame.image.load('uno_card_img/uno_card-red2.png').convert_alpha()
Red3b = pygame.image.load('uno_card_img/uno_card-red3.png').convert_alpha()
Red4b = pygame.image.load('uno_card_img/uno_card-red4.png').convert_alpha()
Red5b = pygame.image.load('uno_card_img/uno_card-red5.png').convert_alpha()
Red6b = pygame.image.load('uno_card_img/uno_card-red6.png').convert_alpha()
Red7b = pygame.image.load('uno_card_img/uno_card-red7.png').convert_alpha()
Red8b = pygame.image.load('uno_card_img/uno_card-red8.png').convert_alpha()
Red9b = pygame.image.load('uno_card_img/uno_card-red9.png').convert_alpha()
RedDraw2b = pygame.image.load('uno_card_img/uno_card-reddraw2.png').convert_alpha()
RedReverseb = pygame.image.load('uno_card_img/uno_card-redreverse.png').convert_alpha()
RedSkipb = pygame.image.load('uno_card_img/uno_card-redskip.png').convert_alpha()



Blue0a = pygame.image.load('uno_card_img/uno_card-blue0.png').convert_alpha()
Blue1a = pygame.image.load('uno_card_img/uno_card-blue1.png').convert_alpha()
Blue2a = pygame.image.load('uno_card_img/uno_card-blue2.png').convert_alpha()
Blue3a = pygame.image.load('uno_card_img/uno_card-blue3.png').convert_alpha()
Blue4a = pygame.image.load('uno_card_img/uno_card-blue4.png').convert_alpha()
Blue5a = pygame.image.load('uno_card_img/uno_card-blue5.png').convert_alpha()
Blue6a = pygame.image.load('uno_card_img/uno_card-blue6.png').convert_alpha()
Blue7a = pygame.image.load('uno_card_img/uno_card-blue7.png').convert_alpha()
Blue8a = pygame.image.load('uno_card_img/uno_card-blue8.png').convert_alpha()
Blue9a = pygame.image.load('uno_card_img/uno_card-blue9.png').convert_alpha()
BlueDraw2a = pygame.image.load('uno_card_img/uno_card-bluedraw2.png').convert_alpha()
BlueReversea = pygame.image.load('uno_card_img/uno_card-bluereverse.png').convert_alpha()
BlueSkipa = pygame.image.load('uno_card_img/uno_card-blueskip.png').convert_alpha()

Blue0b = pygame.image.load('uno_card_img/uno_card-blue0.png').convert_alpha()
Blue1b = pygame.image.load('uno_card_img/uno_card-blue1.png').convert_alpha()
Blue2b = pygame.image.load('uno_card_img/uno_card-blue2.png').convert_alpha()
Blue3b = pygame.image.load('uno_card_img/uno_card-blue3.png').convert_alpha()
Blue4b = pygame.image.load('uno_card_img/uno_card-blue4.png').convert_alpha()
Blue5b = pygame.image.load('uno_card_img/uno_card-blue5.png').convert_alpha()
Blue6b = pygame.image.load('uno_card_img/uno_card-blue6.png').convert_alpha()
Blue7b = pygame.image.load('uno_card_img/uno_card-blue7.png').convert_alpha()
Blue8b = pygame.image.load('uno_card_img/uno_card-blue8.png').convert_alpha()
Blue9b = pygame.image.load('uno_card_img/uno_card-blue9.png').convert_alpha()
BlueDraw2b = pygame.image.load('uno_card_img/uno_card-bluedraw2.png').convert_alpha()
BlueReverseb = pygame.image.load('uno_card_img/uno_card-bluereverse.png').convert_alpha()
BlueSkipb = pygame.image.load('uno_card_img/uno_card-blueskip.png').convert_alpha()



Green0a = pygame.image.load('uno_card_img/uno_card-green0.png').convert_alpha()
Green1a = pygame.image.load('uno_card_img/uno_card-green1.png').convert_alpha()
Green2a = pygame.image.load('uno_card_img/uno_card-green2.png').convert_alpha()
Green3a = pygame.image.load('uno_card_img/uno_card-green3.png').convert_alpha()
Green4a = pygame.image.load('uno_card_img/uno_card-green4.png').convert_alpha()
Green5a = pygame.image.load('uno_card_img/uno_card-green5.png').convert_alpha()
Green6a = pygame.image.load('uno_card_img/uno_card-green6.png').convert_alpha()
Green7a = pygame.image.load('uno_card_img/uno_card-green7.png').convert_alpha()
Green8a = pygame.image.load('uno_card_img/uno_card-green8.png').convert_alpha()
Green9a = pygame.image.load('uno_card_img/uno_card-green9.png').convert_alpha()
GreenDraw2a = pygame.image.load('uno_card_img/uno_card-greendraw2.png').convert_alpha()
GreenReversea = pygame.image.load('uno_card_img/uno_card-greenreverse.png').convert_alpha()
GreenSkipa = pygame.image.load('uno_card_img/uno_card-greenskip.png').convert_alpha()

Green0b = pygame.image.load('uno_card_img/uno_card-green0.png').convert_alpha()
Green1b = pygame.image.load('uno_card_img/uno_card-green1.png').convert_alpha()
Green2b = pygame.image.load('uno_card_img/uno_card-green2.png').convert_alpha()
Green3b = pygame.image.load('uno_card_img/uno_card-green3.png').convert_alpha()
Green4b = pygame.image.load('uno_card_img/uno_card-green4.png').convert_alpha()
Green5b = pygame.image.load('uno_card_img/uno_card-green5.png').convert_alpha()
Green6b = pygame.image.load('uno_card_img/uno_card-green6.png').convert_alpha()
Green7b = pygame.image.load('uno_card_img/uno_card-green7.png').convert_alpha()
Green8b = pygame.image.load('uno_card_img/uno_card-green8.png').convert_alpha()
Green9b = pygame.image.load('uno_card_img/uno_card-green9.png').convert_alpha()
GreenDraw2b = pygame.image.load('uno_card_img/uno_card-greendraw2.png').convert_alpha()
GreenReverseb = pygame.image.load('uno_card_img/uno_card-greenreverse.png').convert_alpha()
GreenSkipb = pygame.image.load('uno_card_img/uno_card-greenskip.png').convert_alpha()



Yellow0a = pygame.image.load('uno_card_img/uno_card-yellow0.png').convert_alpha()
Yellow1a = pygame.image.load('uno_card_img/uno_card-yellow1.png').convert_alpha()
Yellow2a = pygame.image.load('uno_card_img/uno_card-yellow2.png').convert_alpha()
Yellow3a = pygame.image.load('uno_card_img/uno_card-yellow3.png').convert_alpha()
Yellow4a = pygame.image.load('uno_card_img/uno_card-yellow4.png').convert_alpha()
Yellow5a = pygame.image.load('uno_card_img/uno_card-yellow5.png').convert_alpha()
Yellow6a = pygame.image.load('uno_card_img/uno_card-yellow6.png').convert_alpha()
Yellow7a = pygame.image.load('uno_card_img/uno_card-yellow7.png').convert_alpha()
Yellow8a = pygame.image.load('uno_card_img/uno_card-yellow8.png').convert_alpha()
Yellow9a = pygame.image.load('uno_card_img/uno_card-yellow9.png').convert_alpha()
YellowDraw2a = pygame.image.load('uno_card_img/uno_card-yellowdraw2.png').convert_alpha()
YellowReversea = pygame.image.load('uno_card_img/uno_card-yellowreverse.png').convert_alpha()
YellowSkipa = pygame.image.load('uno_card_img/uno_card-yellowskip.png').convert_alpha()

Yellow0b = pygame.image.load('uno_card_img/uno_card-yellow0.png').convert_alpha()
Yellow1b = pygame.image.load('uno_card_img/uno_card-yellow1.png').convert_alpha()
Yellow2b = pygame.image.load('uno_card_img/uno_card-yellow2.png').convert_alpha()
Yellow3b = pygame.image.load('uno_card_img/uno_card-yellow3.png').convert_alpha()
Yellow4b = pygame.image.load('uno_card_img/uno_card-yellow4.png').convert_alpha()
Yellow5b = pygame.image.load('uno_card_img/uno_card-yellow5.png').convert_alpha()
Yellow6b = pygame.image.load('uno_card_img/uno_card-yellow6.png').convert_alpha()
Yellow7b = pygame.image.load('uno_card_img/uno_card-yellow7.png').convert_alpha()
Yellow8b = pygame.image.load('uno_card_img/uno_card-yellow8.png').convert_alpha()
Yellow9b = pygame.image.load('uno_card_img/uno_card-yellow9.png').convert_alpha()
YellowDraw2b = pygame.image.load('uno_card_img/uno_card-yellowdraw2.png').convert_alpha()
YellowReverseb = pygame.image.load('uno_card_img/uno_card-yellowreverse.png').convert_alpha()
YellowSkipb = pygame.image.load('uno_card_img/uno_card-yellowskip.png').convert_alpha()



wild1 = pygame.image.load('uno_card_img/uno_card-wildchange.png').convert_alpha()
wild2 = pygame.image.load('uno_card_img/uno_card-wildchange.png').convert_alpha()
wild3 = pygame.image.load('uno_card_img/uno_card-wildchange.png').convert_alpha()
wild4 = pygame.image.load('uno_card_img/uno_card-wildchange.png').convert_alpha()

wilddraw1 = pygame.image.load('uno_card_img/uno_card-wilddraw4.png').convert_alpha()
wilddraw2 = pygame.image.load('uno_card_img/uno_card-wilddraw4.png').convert_alpha()
wilddraw3 = pygame.image.load('uno_card_img/uno_card-wilddraw4.png').convert_alpha()
wilddraw4 = pygame.image.load('uno_card_img/uno_card-wilddraw4.png').convert_alpha()


Blue0a = button.Button(0, 0, Blue0a, 0.25)
Blue1a = button.Button(30, 0, Blue1a, 0.25)
Blue2a = button.Button(60, 0, Blue2a, 0.25)
Blue3a = button.Button(90, 0, Blue3a, 0.25)
Blue4a = button.Button(120, 0, Blue4a, 0.25)
Blue5a = button.Button(150, 0, Blue5a, 0.25)
Blue6a = button.Button(180, 0, Blue6a, 0.25)
Blue7a = button.Button(210, 0, Blue7a, 0.25)
Blue8a = button.Button(240, 0, Blue8a, 0.25)
Blue9a = button.Button(270, 0, Blue9a, 0.25)
BlueDraw2a = button.Button(300, 0, BlueDraw2a, 0.25)
BlueReversea = button.Button(330, 0, BlueReversea, 0.25)
BlueSkipa = button.Button(360, 0, BlueSkipa, 0.25)

Blue0b = button.Button(390, 0, Blue0b, 0.25)
Blue1b = button.Button(420, 0, Blue1b, 0.25)
Blue2b = button.Button(450, 0, Blue2b, 0.25)
Blue3b = button.Button(480, 0, Blue3b, 0.25)
Blue4b = button.Button(510, 0, Blue4b, 0.25)
Blue5b = button.Button(540, 0, Blue5b, 0.25)
Blue6b = button.Button(570, 0, Blue6b, 0.25)
Blue7b = button.Button(600, 0, Blue7b, 0.25)
Blue8b = button.Button(630, 0, Blue8b, 0.25)
Blue9b = button.Button(660, 0, Blue9b, 0.25)
BlueDraw2b = button.Button(690, 0, BlueDraw2b, 0.25)
BlueReverseb = button.Button(720, 0, BlueReverseb, 0.25)
BlueSkipb = button.Button(750, 0, BlueSkipb, 0.25)



def draw_window():
    screen.fill(ORANGE)

    Blue0a.draw(screen)
    Blue1a.draw(screen)
    Blue2a.draw(screen)
    Blue3a.draw(screen)
    Blue4a.draw(screen)
    Blue5a.draw(screen)
    Blue6a.draw(screen)
    Blue7a.draw(screen)
    Blue8a.draw(screen)
    Blue9a.draw(screen)
    BlueDraw2a.draw(screen)
    BlueReversea.draw(screen)
    BlueSkipa.draw(screen)
    
    Blue0b.draw(screen)
    Blue1b.draw(screen)
    Blue2b.draw(screen)
    Blue3b.draw(screen)
    Blue4b.draw(screen)
    Blue5b.draw(screen)
    Blue6b.draw(screen)
    Blue7b.draw(screen)
    Blue8b.draw(screen)
    Blue9b.draw(screen)
    BlueDraw2b.draw(screen)
    BlueReverseb.draw(screen)
    BlueSkipb.draw(screen)

def main():
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(FPS)
        draw_window()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        pygame.display.update()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()