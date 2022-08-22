import csv
dict={}
list1=[]
list2=[]
with open('users.csv', 'r', newline='') as file:
   reader = csv.reader(file, delimiter= ' ', quotechar=',')
   for row in reader:
     string=(' '.join(row))
     list1.append(string.replace(',',' '))

with open('hobby.csv', 'r', newline='') as file:
   reader = csv.reader(file, delimiter= ' ', quotechar=',')
   for row in reader:
     string=(' '.join(row))
     list2.append(string)

if len(list1) >= len(list2):
  count=0
  while count < len(list1):
    if count < len(list2):
      dict[list1[count]]=list2[count]
    else:
      dict[list1[count]]='None'
    count=count+1
  with open('out.txt','w') as out:
    for key,value in dict.items():
        out.write('{}:{}\n'.format(key,value))
else:
  raise SystemExit(1)
print('Записанные значения: \n', dict)
     
    
