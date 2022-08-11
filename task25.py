price = [10.6, 48, 52, 31, 46, 37, 78.3, 54.06, 99.99]
price.sort()
for i in price:
    a = str(i)
    if a.__contains__('.'):
        list = a.split('.')
        if len(list[1]) < 2:
          print(list[0] + ' руб' + ' 0' + list[1] + ' коп')
        else:
          print(list[0] + ' руб' + ' ' + list[1] + ' коп')
    else:
        print(a + ' руб 00 коп')

print(price is price)

print('======================')
new_price = price
new_price.sort(reverse=True)

for i in new_price:
    a = str(i)
    if a.__contains__('.'):
        list = a.split('.')
        if len(list[1]) < 2:
          print(list[0] + ' руб' + ' 0' + list[1] + ' коп')
        else:
          print(list[0] + ' руб' + ' ' + list[1] + ' коп')
    else:
        print(a + ' руб 00 коп')
