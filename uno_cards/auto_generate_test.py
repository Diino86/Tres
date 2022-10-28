import pygame
import random
import time
from button import *
from display import menu_display
from card_objects import card_objects

class deck:
    def __init__(self):
        self.cards = []
        colors = ['red', 'blue', 'green', 'yellow']
        special = ['draw2', 'reverse', 'skip']
        unique = ['wildchange', 'wilddraw4']
        
        
        for color in colors:
            for zero in range(1):
                self.cards.append(card(zero, color))

        for _ in range(2):
            for color in colors:
                for number in range(1, 10):
                    self.cards.append(card(number, color))
                    
        for _ in range(2):
            for color in colors:
                for s in special:
                    self.cards.append(card(s, color))
        
        for _ in range(4):
            for u in unique:
                self.cards.append(card(u, ''))
        
        random.shuffle(self.cards)
        
    def add(self, card):
        self.cards.insert(0, card.remove())
        
    def remove(self):
        return self.cards.pop()


class player:
    def __init__(self, name, y):
        self.player_deck = []
        self.name = name
        self.y = y

    def draw(self, deck):
        self.player_deck.append(deck.remove())
        
    # add your {input} to .pop(input)
    def play(self, index):
        return self.player_deck.pop(index)


class pile(card_objects):
    def __init__(self):
        self.card = []
        
    def add(self, cards, index):
        self.card.insert(0, cards.play(index))
        
    def beginning_add(self, cards):
        self.card.insert(0, cards.remove())
        
    def remove(self):
        return self.card.pop()


class game_menu(menu_display, card_objects):
    def __init__(self):
        menu_display.__init__(self)
        card_objects.__init__(self)
        self.p1 = player('User1', 550)
        self.p2 = player('User2', 50)
        self.card_space = 70
        self.menu3_RUNNING = True
        self.exit_game_img = img('exit-game_button')
        self.exit_game_button = Button(980, 20, self.exit_game_img.image, 0.35)
        self.turn = 1
        
        self.pile = pile()
        self.deck = deck()
        self.pile_img = card('', 'back')
        
        for _ in range(7):
            self.p1.draw(self.deck)
            self.p2.draw(self.deck)
        
        self.first_card()
            
    def first_card(self):
        x = self.pile.beginning_add(self.deck)
        while True:
            if x == self.wild1:
                self.pile.add(self.deck)
            elif x == self.wilddraw4:
                self.pile.add(self.deck)
            else:
                break
        
    def screen_feature(self):
        self.clock.tick(self.FPS)
        self.screen.fill(self.ORANGE)
        
        if self.pile_img.draw(725, 280, self.screen) == True:
                if self.turn == 1:
                    self.turn = 2
                    self.p1.draw(self.deck)
                elif self.turn == 2:
                    self.turn = 1
                    self.p2.draw(self.deck)
                
        if self.exit_game_button.draw(self.screen) == True:
                time.sleep(0.1)
                self.menu3_RUNNING = False
                
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu3_RUNNING = False
                    
                
    def card_display(self, player):
        x = (self.WIDTH/2 - ((102.5 + ((self.count(player.player_deck) - 1) * self.card_space))/2)) - self.card_space
        for card in player.player_deck:
            x += self.card_space
            if card.draw(x, player.y, self.screen) == True:
                if self.turn == 1:
                    self.turn = 2
                elif self.turn == 2:
                    self.turn = 1
                self.pile.add(player, player.player_deck.index(card))
            
    def count(self, cards):
        n = 0
        for x in cards:
            n += 1
        return n
        
    def main(self):
        while self.menu3_RUNNING:
            self.screen_feature()
            self.pile.card[0].draw(455, 280, self.screen)
            if self.turn == 1:
                self.card_display(self.p1)
            elif self.turn == 2:
                self.card_display(self.p2)

                
            pygame.display.update()
# Temporal____________
#         pygame.quit()
# 
# g = game_menu()
# g.main()
