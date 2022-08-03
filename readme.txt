# pythonpractice task 1.1
В данной программе реализовать цикл не получилось, выдает ошибку при вводе пустого значения:Traceback (most recent call last):
  File "main.py", line 2, in <module>
    duration = int(input('duration='))
ValueError: invalid literal for int() with base 10: ''
  
  Код для цикла использовался такой: 
  while True:
 duration = int(input('duration='))
 if duration == "":
  break
