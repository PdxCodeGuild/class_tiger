#dict_practice.py
product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
product_to_price['apple']  #> 1.0
product_to_price['grapes']  #> 0.75
#product_to_price[1.0]  # Throws KeyError
product_to_price['banana']=2.0
#(product_to_price.get('peach', 3.0))

product_to_price['banana'] = 0.25
product_to_price = {'apple': 1.0, 'pear': 1.5, 'banana': 0.25, 'grapes': 0.75}
for item in product_to_price.items():
    print(item)
fruits = ['pear', 'apple', 'grapes']
prices = [0.75, 1.0, 1.5]
product_to_price = dict(zip(fruits, prices))
print(product_to_price)
