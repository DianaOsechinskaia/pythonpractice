import sys
from pandas import read_csv

if len(sys.argv) == 1:
  out = read_csv('bakery.csv')
  out.index += 1
  print(out)
if len(sys.argv) == 2:
  count = int(sys.argv[1])
  out = read_csv('bakery.csv', skiprows=count)
  out.index += 1
  print(out)

if len(sys.argv) == 3:
  first_count = int(sys.argv[1])
  second_count = int(sys.argv[2])
  out = read_csv('bakery.csv', skiprows=first_count,nrows = second_count)
  out.index += 1
  print(out)
