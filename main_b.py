import random
BLUE = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

class color:
    BLUE = '\033[96m'
    GREEN = '\033[91m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'



red = color.RED
blue = color.BLUE
green = color.GREEN
yellow = color.YELLOW
end = color.ENDC

# colors = ["Red","Green","Yellow","Blue"]
# colors = [xredx,xgreenx,xyellowx,xbluex]
colors = [red,green,yellow,blue]
values = [0,1,2,3,4,5,6,7,8,9,"dr2","sk","rv",]
unique = ["w","wd4"]


#Funktion som numrerar de distruberade korten
def playerCards(player, playerCard):
    print("\n\033[0mPlayer {}'s cards: ".format(player + 1))
    print("")
    c = 1
    for card in playerCard:
        print(f'\033[0m{c})|{card} |')
        c+=1
    print("\n\033[0m")
    count(TresDeck)
    print ("")

#funktion som distribuerar ett visst antal kort till ett visst antal spelare.
def Distribute(cards):
    DrawnCards = []
    for x in range(cards):
        DrawnCards.append(TresDeck.pop(0))
    return DrawnCards

def Tres():
    deck = []
    colors = [red,green,yellow,blue]
    values = [0,1,2,3,4,5,6,7,8,9,"dr2","sk","rv",]
    unique = [" w"," wd4"]


    for color in colors:
        for value in values:
            PlayerCard = "{} {}".format(color, value)
            deck.append(PlayerCard)
            if value != 0:
                deck.append(PlayerCard)

    for u in range(4):
        deck.append(unique[0])
        deck.append(unique[1])


    random.shuffle(deck)
    return deck
#checkar om spelaren kan spela.
#Bolean är enklast (enligt stackoverflow haha), då den
#endast returnerar sant eller falskt (1 eller 0). 
def Rules(color, value, playerCards):
    for card in playerCards:
        if "w" in card:
            return True
        elif value in card or color in card:
            return True
        elif color and value in card:
            return True
    return False



def count(cards):
    n = 0
    for x in cards:
        n += 1

    print(f'Cards: {n}')






TresDeck = Tres()

#Discards: en lista med ukastade kort. Kan sedan användas för att visa det -->
#kort högst i "högen"
discards = []


print("Welcome to Tres!\n")
print('sk = skipp\nrv = reverse\ndr2 = draw 2')
print('w = wild\nwd4 = wild draw 4\n')
count(TresDeck)
players = []

numPL = int(input("How many players?: "))
print("----------------")

while  numPL>4 or numPL<2:
    numPL = int(input("Invalid. How many players?: "))

for player in range(numPL):
    players.append(Distribute(2))





#Två variabler som styr spelarnas tur (p_turn) och deras direction (p_turn).
#Kan manipuleras för att senare kunna verkställa sk samt rv korten. 
p_direc = 1
p_turn = 0
discards.append(TresDeck.pop(0))
#splitrar kortet för att senare undersöka innehållet. Returnerar en lista.
#Problem om färger används??
CardSplit = discards[0].split(" ", 1)
C_color = CardSplit[0]

if C_color != "w":
    PlayerCard = CardSplit[1]
else:
    PlayerCard = "Any" #Behövs fixas
w = "Player {}".format(p_turn+1)

playing = True
while playing:
    #each players Cards numbered til Distribute(x) 
    playerCards(p_turn, players[p_turn])
    print("\033[0mCard on top:|{} |".format(discards[-1])) #-1 bättre än 0 --> alltid visa sista kortet

    #kollar först Rules(), eller om det går att spela (bolean). Sant -->
    #det under sker. Falskt --> else: verkställs.
    if Rules(C_color, PlayerCard, players[p_turn]):
    #bug:allt kan skrivas. Fixa --> endast integer och C_color ska ej vara  större elle mindre spelarens antal kort.
        Chosen_C = int(input("\033[0mWhich card do you want to play?: ")) 
        #då det falskt, utförst funktionen.
        #Tredje spalten, returnerar en lista där p_turn (spelarnas) kort hämtas
        #och sedan subtraheras det valde kortet med 1, då det är lista, index så 
        #för spelaren börjar det från 0.
        while not Rules(C_color, PlayerCard, [players[p_turn][Chosen_C-1]]):
                Chosen_C = int(input("\033[0mNot valid. Which card do you want to play?: "))
        print(f'\n\033[0mYou played: |{players[p_turn][Chosen_C-1]}\033[0m |')
        print("\n----------------")

        discards.append(players[p_turn].pop(Chosen_C-1))
        if len(players[p_turn])==0:
            playing = False
            w = "\033[0mPlayer {}".format(p_turn+1)
            
        else:
            CardSplit = discards[-1].split(" ", 1)
            C_color = CardSplit[0]
            if len(CardSplit) == 1:
                PlayerCard = "Any"  #????
            else:
                PlayerCard = CardSplit[1]
            if C_color == "w":
                for x in range(len(colors)):
                    print("{}) {}".format(x+1, print(colors[x])))   #Funkar ej
                new_C = int(input("\033[0mChoose a color: "))
                print()
                while new_C < 1 or new_C > 4:
                    new_C = int(input("\033[0mInvalid option. What colour would you like to choose?"))
                    print("\033[0mYou chose {}".format(print(colors[x])))
                C_color = colors[new_C-1]
                print("\033[0mYou chose the color: {}".format(C_color)) 
            #multiplicerar ordningen med -1 --> går åt andra hållet.
            if PlayerCard == "rv":
                p_direc = p_direc * -1
                p_turn = p_direc
            #skippar nästa spelare
            elif PlayerCard == "sk":
                p_turn += p_direc
                if p_turn >= numPL:
                    p_turn = 0
                elif p_turn < 0:
                    p_turn = numPL-1
            #tar upp två kort om summan av p_turn och p_dir är mindre än 0.
            elif PlayerCard == "dr2":
                p_draw = p_turn + p_direc
                if p_draw == numPL:
                    p_draw = 0
                elif p_draw < 0:
                    p_draw = numPL-1
                print("\033[0mDraw 2 cards.")
                players[p_draw] = players[p_draw] + Distribute(2)
            #samma princip som dr2 men tar upp 4 kort.
            elif PlayerCard == "dr4":
                p_draw = p_turn+p_direc
                if p_draw == numPL:
                    p_draw = 0
                elif p_draw < 0:
                    p_draw = numPL-1
                print("\033[0mDraw 4 cards.")
                players[p_draw] = players[p_draw] + Distribute(4)

            print("")
    else:
        print("\033[0mDraw a card.")
        players[p_turn] = players[p_turn] + Distribute(1)


    #öka splarens tur (värdet) med direction-
    p_turn += p_direc
    #loopar om. nollställer om likheten uppfylls
    if p_turn == numPL:
        p_turn = 0
    elif p_turn < 0:
        p_turn = numPL-1
print("\n\033[0mTREEEEEES!!!\n\nGame Over!\n")
print(f"\033[0m{w} is the winner!!!")