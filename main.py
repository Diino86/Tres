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

    #72 cards - Type 1-9
    for _ in range(2):
        for color in colors:
            for number in range(1, 10):
                cards.append((number, color))
                
    #16 cards - Type special
    for _ in range(2):
        for color in colors:
            for s in special:
                cards.append((s, color))
                
    #8 cards - type unique
    for _ in range(4):
        for u in unique:
            cards.append((u, None))
            
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
    print(player_cards)
    return player_cards

    
red = color.RED
blue = color.BLUE
green = color.GREEN
yellow = color.YELLOW
end = color.ENDC

def showCards(cards):
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    color = ['r', 'b', 'g', 'y']
    for card in cards:
        if card[0] in number and card[1] == 'r':
            print(f'{red}test{end}')
        elif card[0] in number and card[1] == 'b':
            print(f'{blue}test{end}')
        elif card[0] in number and card[1] == 'g':
            print(f'{green}test{end}')
        elif card[0] in number and card[1] == 'y':
            print(f'{yellow}test{end}')
        else:
            print('Coming soon')

card_pile = cards()
main()