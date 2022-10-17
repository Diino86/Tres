import random

class color:
    BLUE = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

def main():
    count(card_pile)
    player1 = player(distribute(card_pile))
    showCards((player1))

#Cards_________________________________________________
def cards():
    print('sk = skipp\nrv = reverse\ndr2 = draw 2\nw = wild\nwdr4 = Wild Draw 4\n')
    cards = []
    colors = ['r', 'b', 'g', 'y']
    special = ['sk', 'rv', 'dr2']
    unique = ['w', 'wdr4']
    
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
        for s in unique:
            cards.append((s, 'none'))
            
    random.shuffle(cards)
    return cards
#_______________________________________________________

def count(cards):
    n = 0
    for x in cards:
        n += 1
    
    print(f'Cards: {n}')


def distribute(d_cards):
    player_deck = []
    for x in range(7):
        player_deck.append(d_cards.pop())
    return player_deck


def player(p_cards):
    player_cards = p_cards
    return player_cards

    
red = color.RED
blue = color.BLUE
green = color.GREEN
yellow = color.YELLOW
end = color.ENDC

def whichCard(list, card_number):
    for n in list:
        if n == card_number:
            return n
        
def whichColor(list, card_color):
    for c in list:
        if c == card_color:
            return list[c]
    
def whichSpecial(list, special_card):
    for s in list:
        if s == special_card:
            return list[s]
        

def showCards(cards):
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    special = {10:'sk', 11:'rv', 12:'dr2'}
    color = {'r':red, 'b':blue, 'g':green, 'y':yellow}
    for card in cards:
        if card[0] in number and card[1] in color:
            Card(whichColor(color, card[1]), whichCard(number, card[0]))
        elif card[0] in special and card[1] in color:
            Card(whichColor(color, card[1]), whichSpecial(special, card[0]))
        else:
            print('Coming soon')
            
def Card(color, number):
    print(f'{color}{number}{end}')

card_pile = cards()
main()