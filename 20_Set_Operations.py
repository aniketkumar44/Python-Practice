#sets (fruits)
basket={'apple','orange','apple','pear','orange','banana'}
print("Basket = ",basket)
print('orange' in basket)
print('grapes' in basket)
print("Basket Len = ",len(basket))
print("Basket in sort = ",sorted(basket))

#sets
a=set('abrakadabra')
print("a = ",a)
b=set('alexander')
print("b = ",b)
print(a-b)
print(b-a)
print(a&b)
print(a|b)
