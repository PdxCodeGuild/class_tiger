def advise(card):
    if card == 'A' or 'a':
        return 1
    elif card in ['J','Q','K','j','k','q']:
        return 10
    else:
        return int(card)


def guess_game():
    input1= input(f'What\'s your first card? ')
    input2= input(f'What\'s your second card?  ')
    input3= input(f'What\'s your third card? ')
    Total = advise(input1) + advise(input2) + advise(input3)
    if Total < 17:
        return (f'{Total} Hit!')
    elif  17 <= Total < 21:
        return (f'{Total} Stay!')
    elif Total == 21:
        return (f'{Total} Blackjack!')
    elif Total > 21:
        return (f'{Total} Almost Busted!')

guess_game()