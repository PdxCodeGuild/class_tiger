'''
Lab 19: Blackjack Advice
Write a program to give basic blackjack advice. First ask the user for three playing cards. Then figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10.

less than 17 advise 'hit'
greater than or equal to 17 , but less than 21 advise 'stay'
exactly 21 advise 'blackjack!'
over 21 advise 'Already Busted'
'''
card_points = {'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
card1 = input('What is your first card? > ').upper()
card2 = input('What is your second card? > ').upper()
card3 = input('What is your third card? > ').upper()

def advise_hand(card1,card2,card3):

    list_cards = [card1,card2,card3]


    sum_cards = card_points[card1] + card_points[card2] + card_points[card3]
    print(sum_cards)

    if sum_cards > 21 and 'A' in list_cards:
        print('Ace Conversion')
        sum_cards = sum_cards - 10
        print(sum_cards)


    def check_hand(sum_cards):
        if sum_cards < 17:
            advice = 'Hit!'
            return advice
        elif sum_cards >= 17 and sum_cards < 21:
            advice = 'Stay'
            return advice
        elif sum_cards == 21:
            advice = "Blackjack!"
            return advice
        elif sum_cards > 21:
            advice = "Busted!"
            return advice
        else:
            print("somethin went wrong")

    advice = check_hand(sum_cards)
    return advice



print(advise_hand(card1,card2,card3))
