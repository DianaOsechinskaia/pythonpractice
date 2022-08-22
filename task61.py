
try:
  with open('nginx_logs.txt', 'r',encoding="utf-8") as file:
    txt = file.read()
    print('Success!')
except FileNotFoundError:
  print('Для начала скачайте файл')


result = [(lambda x: (x[0],x[5][1:],x[6]))(line.split()) for line in txt.split('\n') if line]
print(result)
