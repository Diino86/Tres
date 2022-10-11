def cards():
    cards = []
    colors = ['red', 'blue', 'green', 'yellow']
    special = ['skip', 'reverse', 'draw2']
    unique = ['wild', 'wilddraw4']
    
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
            
    print(cards)
    return cards