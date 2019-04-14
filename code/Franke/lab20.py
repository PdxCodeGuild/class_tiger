def card_validation():
  Card_Number = input(f'Input your credit card number ')
  Card_Number  = [int(i) for i in Card_Number.split()]
  Check_digit = Card_Number.pop()
  Card_Number.reverse()
  #4Double every other element in the reversed list.
  for i in range(0,len(Card_Number),2):
      Card_Number *= 2
  #5 Subtract nine from numbers over nine.
  for i in Card_Number:
      if i > 9 :
          Card_Number -= 9

  if int(list(str(sum(Card_Number)))[1]) == Check_digit:
             print(f'Valid!')
  else:
    print(f'Invalid!')

