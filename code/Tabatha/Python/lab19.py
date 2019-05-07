# import string

card1 = input("What is your first card? >").lower()
card2 = input("What is your second card? >").lower()
card3 = input("What is your third card? >").lower()

card_value = {"a":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "j":10, "q":10, "k":10}

def black(jack):
    total = card_value[card1] + card_value[card2] + card_value[card3]
    if total < 17:
        return print(f"{total} Hit!")
    elif 16 > total > 21:
        return print(f"{total} Stay")
    elif total == 21:
        return print(f"{total} Blackjack!")
    elif total > 21:
        return print(f"{total} Busted!")
    
print(black(card1))

