#blackjack_advice.py
def card_value(x):
    if (x=='K'or x=='k' or x=='Q'or x=='q' or x=='J' or x=='j'):
        return (10)
    elif (x == 'A'or x== 'a'):
        ace_option=input("Do you want this ace to equal 1 or 11?")
        ace_option = int(ace_option)
        if ace_option == 1:
            return 1
        elif ace_option == 11:
            return 11
        return (ace_option)
    return int(x)


def card_input():
    card_1=input('What is your first card?')
    card_2=input('What is your second card?')
    card_3=input('What is your third card?')

    card_total = card_value(card_1) + card_value(card_2) + card_value(card_3)
    print(card_total)
    if (card_total>= 22):
        print("Busted!")
    elif (card_total == 21):
        print("Blackjack!")
    elif (card_total<=20 and card_total>=16):
        print("Stay")
    else:
        print("Hit")

card_input()
