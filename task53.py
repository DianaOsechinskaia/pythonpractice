tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена','test','test1']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
def list_tutors():
  size = 0
  i = 0
  
  if len(tutors) > len(klasses):
    size = len(tutors)
  else:
    size = len(klasses)
    
  while i <= size:
   if i <= len(tutors) and i >= len(klasses):
     yield(tutors[i], None)
     i = i + 1
     break
   elif i <= len(klasses) and i >= len(tutors):
     yield(None, klasses[i])
     i = i + 1
     break
   else:
       yield(tutors[i], klasses[i])
       i = i + 1


    

for el in list_tutors():
  print(el)
