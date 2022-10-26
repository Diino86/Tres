import pygame
import random
import time
from button import *
from display import menu_display


class player:
    def __init__(self, deck):
        self.deck = deck

class deck:
    def __init__(self):
        self.cards = []
        colors = ['red', 'blue', 'green', 'yellow']
        special = ['draw2', 'reverse', 'skip']
        unique = ['wildchange', 'wilddraw4']
        
        
        for color in colors:
            for zero in range(1):
                self.cards.append((zero, color))

        for _ in range(2):
            for color in colors:
                for number in range(1, 10):
                    self.cards.append((number, color))
                    
        for _ in range(2):
            for color in colors:
                for s in special:
                    self.cards.append((s, color))
        
        for _ in range(4):
            for u in unique:
                self.cards.append((u, ''))
        
        random.shuffle(self.cards)
        
    def distribute(self):
        self.deck = []
        for x in range(7):
            self.deck.append(self.cards.pop())
        return self.deck



class game_menu(menu_display):
    def __init__(self):
        menu_display.__init__(self)
        self.menu3_RUNNING = True
        
        self.exit_game_img = img('exit-game_button')
        self.exit_game_button = Button(980, 20, self.exit_game_img.image, 0.35)
        
        self.deck = deck()
        self.player1 = player(self.deck.distribute())
        self.player2 = player(self.deck.distribute())
        
        for x in player1:
            self.card = card(x[0], x[1])
        
        self.red0 = card(1, 'red')
        self.red0_card = Button(0, 0, self.red0.image, 0.25)
        
    def main(self):
        while self.menu3_RUNNING:
            self.clock.tick(self.FPS)
            self.screen.fill(self.ORANGE)
            
            self.red0_card.draw(self.screen)
            
            if self.exit_game_button.draw(self.screen) == True:
                time.sleep(0.2)
                self.menu3_RUNNING = False
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu3_RUNNING = False
                    
            pygame.display.update()


red0a = card(0, 'red')
red1a = card(1, 'red')
red2a = card(2, 'red')
red3a = card(3, 'red')
red4a = card(4, 'red')
red5a = card(5, 'red')
red6a = card(6, 'red')
red7a = card(7, 'red')
red8a = card(8, 'red')
red9a = card(9, 'red')
reddraw2a = card('draw2', 'red')
redreversea = card('reverse', 'red')
redskipa = card('skip', 'red')

red0b = card(0, 'red')
red1b = card(1, 'red')
red2b = card(2, 'red')
red3b = card(3, 'red')
red4b = card(4, 'red')
red5b = card(5, 'red')
red6b = card(6, 'red')
red7b = card(7, 'red')
red8b = card(8, 'red')
red9b = card(9, 'red')
reddraw2b = card('draw2', 'red')
redreverseb = card('reverse', 'red')
redskipb = card('skip', 'red')


blue0a = card(0, 'blue')
blue1a = card(1, 'blue')
blue2a = card(2, 'blue')
blue3a = card(3, 'blue')
blue4a = card(4, 'blue')
blue5a = card(5, 'blue')
blue6a = card(6, 'blue')
blue7a = card(7, 'blue')
blue8a = card(8, 'blue')
blue9a = card(9, 'blue')
bluedraw2a = card('draw2', 'blue')
bluereversea = card('reverse', 'blue')
blueskipa = card('skip', 'blue')

blue0b = card(0, 'blue')
blue1b = card(1, 'blue')
blue2b = card(2, 'blue')
blue3b = card(3, 'blue')
blue4b = card(4, 'blue')
blue5b = card(5, 'blue')
blue6b = card(6, 'blue')
blue7b = card(7, 'blue')
blue8b = card(8, 'blue')
blue9b = card(9, 'blue')
bluedraw2b = card('draw2', 'blue')
bluereverseb = card('reverse', 'blue')
blueskipb = card('skip', 'blue')


green0a = card(0, 'green')
green1a = card(1, 'green')
green2a = card(2, 'green')
green3a = card(3, 'green')
green4a = card(4, 'green')
green5a = card(5, 'green')
green6a = card(6, 'green')
green7a = card(7, 'green')
green8a = card(8, 'green')
green9a = card(9, 'green')
greendraw2a = card('draw2', 'green')
greenreversea = card('reverse', 'green')
greenskipa = card('skip', 'green')

green0b = card(0, 'green')
green1b = card(1, 'green')
green2b = card(2, 'green')
green3b = card(3, 'green')
green4b = card(4, 'green')
green5b = card(5, 'green')
green6b = card(6, 'green')
green7b = card(7, 'green')
green8b = card(8, 'green')
green9b = card(9, 'green')
greendraw2b = card('draw2', 'green')
greenreverseb = card('reverse', 'green')
greenskipb = card('skip', 'green')


yellow0a = card(0, 'yellow')
yellow1a = card(1, 'yellow')
yellow2a = card(2, 'yellow')
yellow3a = card(3, 'yellow')
yellow4a = card(4, 'yellow')
yellow5a = card(5, 'yellow')
yellow6a = card(6, 'yellow')
yellow7a = card(7, 'yellow')
yellow8a = card(8, 'yellow')
yellow9a = card(9, 'yellow')
yellowdraw2a = card('draw2', 'yellow')
yellowreversea = card('reverse', 'yellow')
yellowskipa = card('skip', 'yellow')

yellow0b = card(0, 'yellow')
yellow1b = card(1, 'yellow')
yellow2b = card(2, 'yellow')
yellow3b = card(3, 'yellow')
yellow4b = card(4, 'yellow')
yellow5b = card(5, 'yellow')
yellow6b = card(6, 'yellow')
yellow7b = card(7, 'yellow')
yellow8b = card(8, 'yellow')
yellow9b = card(9, 'yellow')
yellowdraw2b = card('draw2', 'yellow')
yellowreverseb = card('reverse', 'yellow')
yellowskipb = card('skip', 'yellow')


wild1 = card('draw2', '')
wild2 = card('draw2', '')
wild3 = card('draw2', '')
wild4 = card('draw2', '')

wilddraw1 = card('draw2', '')
wilddraw2 = card('draw2', '')
wilddraw3 = card('draw2', '')
wilddraw4 = card('draw2', '')