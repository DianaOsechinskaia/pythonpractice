import sys

if len(sys.argv) > 1:
  with open('bakery.csv', 'a') as file:
    file.write(sys.argv[1] + "\n")
else:
  print('Нужно указать прибыль!')