
def num_translate_adv(line):
  word = ''
  for key, value in words_dict.items():
     if key.lower() == line.lower():
      word = value
      return word
  if word == '':
      return word


words_dict = {
  'one':'один',
  'two':'два',
  'three':'три',
  'four':'четыре',
  'five':'пять',
  'six':'шесть',
  'seven':'семь',
  'eight':'восемь',
  'nine':'девять',
  'ten':'десять'
}


while True:
  print('<=============================>')
  print('Напишите какую цифру(от одного до десяти) вы хотите перевести(текст):')

  a = str(input())
  result = num_translate_adv(a)

  if result != '':
    print(result)
  else:
    print('None')
    break






    

