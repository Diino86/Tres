import random

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

def main():
    print('sk = skipp\nrv = reverse\ndr2 = draw 2')
    print('w = wild\nwd4 = wild draw 4\n')
    decks = {}
    #card_pile = cards()
    count(card_pile)
    
    for n in range(playerCount()):
        decks[n+1] = distribute(card_pile)

    showCards(startingCard(card_pile))
    print()
    showCards(decks[1])
    print()
    count(card_pile)
    

#Card Generator______________________________________________________
    #Automatically generates all needed cards
def cards():
    #Available cards:
    #Card number 0-9
    #Special card (10 = Skip   11 = Reverse   12 = Draw 2)
    #Unique card  (13 = Wild   14 = Wild Draw 4)
    
    cards = []
    colors = ['r', 'b', 'g', 'y']
    
    #4 cards - Type 0
    for color in colors:
        for zero in range(1):
            cards.append((zero, color))

    #72 and 24 cards - Type 1-9 and special
    for _ in range(2):
        for color in colors:
            for number in range(1, 13):
                cards.append((number, color))
    
    #8 cards - type unique
    for _ in range(4):
        for u in range(13,15):
            cards.append((u, ''))
            
    random.shuffle(cards)
    return cards
#Card Generator______________________________________________________

#Coming soon_________________________________________________________
    #Count amout of cards for given list(cards)
def count(cards):
    n = 0
    for x in cards:
        n += 1
    
    print(f'Cards: {n}')

    #Input for how many players will play the game
def playerCount():
    players = int(input('Enter the amount of players (1-4): '))
    return players

    #Return a deck of 7 cards from given card list(d_cards)
def distribute(cards):
    deck = []
    for x in range(7):
        deck.append(cards.pop())
    return deck

def startingCard(cards):
    one = []
    while True:
        one.append(cards.pop())
        if one[0] == 14:
            cards.append(one.pop())
            random.shuffle(cards)
        else:
            return one
            break
        
#Coming soon_________________________________________________________

#Find corresponding card number/type and color for each tuple (a, b)_
def showCards(cards):
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    special = {10:'sk', 11:'rv', 12:'dr2'}
    unique = {13:'w', 14:'wd4'}
    color = {'r':red, 'b':blue, 'g':green, 'y':yellow}
    for card in cards:
        if card[0] in number and card[1] in color:
            PrintCard(whichCard(number, card[0]), whichCard(color, card[1]))
        elif card[0] in special and card[1] in color:
            PrintCard(whichCard(special, card[0]), whichCard(color, card[1]))
        elif card[0] in unique:
            PrintCard(whichCard(unique, card[0]), '')
        else:
            print('Coming soon')
            
    #Find card number/color/type for given list(list)
def whichCard(list, card_attribute):
    for a in list:
        if a == card_attribute:
            return list[a]

#Print card so the player can see it
def PrintCard(number, color):
    print(f'{color}|{number}|{end}', end=' ')
#Find corresponding card number/type and color for each tuple (a, b)_

def yourPlayer():
    pass

card_pile = cards()
main()