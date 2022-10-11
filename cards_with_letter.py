def cards():
    cards = []
    colors = ['red', 'blue', 'green', 'yellow']
    special = ['skip', 'reverse', 'draw2']
    unique = ['wild', 'wilddraw4']
    
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
                
    #8 cards - Type unique
    for _ in range(4):
        for s in unique:
            cards.append((s, None))
            
    print(cards)
    return cards