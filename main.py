
duration = int(input('duration='))
if duration < 60:
  print(duration, 'сек')

if duration > 60 and duration < 3600:
   if duration % 60 == 0: 
     min = duration // 60
     print(min,'мин')
   else:
    min = duration // 60
    sec = duration % 60
    print(min,'мин',sec,'сек')

if  duration >= 3600 and duration < 86400:
   hour = duration // 3600
   min = (duration -  hour*3600) // 60
   sec = duration - hour*3600 - min*60
   print(hour,'ч',min,'мин',sec,'сек')


if  duration >=86400:
  day = duration // 86400
  hour = (duration - day*86400) // 3600
  min = (duration - day*86400 -  hour*3600) // 60
  sec = duration - day*86400 - hour*3600 - min*60
  print(day, 'дн',hour,'ч',min,'мин',sec,'сек')

  

