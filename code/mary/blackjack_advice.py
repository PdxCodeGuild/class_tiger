#blackjack_advice.py
def card_value(x):
    if (x==2,3,4,5,6,7,8,9,10):
        return card_value(x)
    elif (x=='K', x=='Q', x=='J'):
        return card_value(10)
    elif (x == 'A'):
        return card_value(1)
    return int(x)


def card_input():
    card_1=input('What is your first card?')
    card_2=input('What is your second card?')
    card_3=input('What is your third card?')
    print(card_total(card_value(card_1)+card_value(card_2)+card_value(card_3))
