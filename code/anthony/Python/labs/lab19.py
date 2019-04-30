def main():
    card1 = get_card("What's your first card? ")
    card2 = get_card("What's your second card? ")
    card3 = get_card("What's your third card? ")

    advice(card1, card2, card3)

def get_card(prompt):
    card_choices = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
    user_input = input(f"{prompt}")
    
    while user_input not in card_choices:
       user_input = input(f"{prompt}")
    return card_choices[user_input]       

def advice(card1, card2, card3):
    card_total = card1 + card2 + card3
    if card_total == 21:
        print(f"{card_total} Blackjack!")
    elif card_total > 21:
        print("Already Busted")
    elif card_total < 17:
        print(f"{card_total} Hit")
    else:
        print(f"{card_total} Stay")

    
main()