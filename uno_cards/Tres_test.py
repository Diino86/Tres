import random
import pygame

class color:
    BLUE = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    
red = color.RED
blue = color.BLUE
green = color.GREEN
yellow = color.YELLOW
end = color.ENDC


class player:
    def __init__(self, deck):
        self.deck = deck

class card:
    def __init__(self, number, color, image):
        self.number = number
        self.color = color
        self.image = pygame.image.load('uno_card_img/uno_card-' + str(self.number) + str(self.color) + '.png')
        
    


class deck:
    def __init__(self):    
        colors = ['red', 'blue', 'green', 'yellow']
        self.cards = []
        
        for color in colors:
            for zero in range(1):
                self.cards.append((zero, color))

        for _ in range(2):
            for color in colors:
                for number in range(1, 13):
                    self.cards.append((number, color))
        
        for _ in range(4):
            for unique in range(13,15):
                self.cards.append((unique, ''))
        
        random.shuffle(self.cards)
        
    def show(self):
        print(self.cards)
        
    def distribute(self):
        self.deck = []
        for x in range(7):
            self.deck.append(self.cards.pop())
        return self.deck


class pile:
    pass


class gameEngine:
    pass


deck = deck()
player1 = player(deck.distribute())
player2 = player(deck.distribute())