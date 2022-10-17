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
    print('w = wild\nwdr4 = Wild Draw 4\n')
    player1 = []
    player2 = []
    player3 = []
    player4 = []
    
    card_pile = cards()
    count(card_pile)
    
#     for n in playerCount:
        
    player1 = distribute(card_pile)
    print(player1)
    showCards((player1))


#Card Generator______________________________________________________
    #Automatically generates all needed cards
def cards():
    cards = []
    colors = ['r', 'b', 'g', 'y']
    #Special (10 = Skip   11 = Reverse   12 = Draw 2)
    #Unique  (13 = Wild   14 = Wild Draw 4)
    
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
            cards.append((u, None))
            
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
def distribute(d_cards):
    deck = []
    for x in range(7):
        deck.append(d_cards.pop())
    return deck

    #Coming soon
def player(p_cards):
    player_cards = p_cards
    return player_cards
#Coming soon_________________________________________________________

#Find corresponding card number/type and color for each tuple (a, b)_
def showCards(cards):
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    special = {10:'sk', 11:'rv', 12:'dr2'}
    unique = {13:'w', 14:'wdr4'}
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
    print(f'{color}{number}{end}')
#Find corresponding card number/type and color for each tuple (a, b)_

main()

