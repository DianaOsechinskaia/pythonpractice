line_list=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
char = '+'
line = ''

for element in line_list:
  try:
    try:
        float(element)
        if element.startswith(char):
         print("'" + element[0] + '0' + element[1] + "'")
         line += "'" + element[0] + '0' + element[1] + "'" + ' '
        else:
            if len(element) == 1:
                print("'" + '0' + element +"'")
                line += "'" + '0' + element +"'" + ' '
            else:
               print("'" + element + "'")
               line += "'" + element + "'" + ' '
    except:
        int(element)
        if element.startswith(char):
         print("'" + element[0] + '0' + element[1] + "'")
         line += "'" + element[0] + '0' + element[1] + "'" + ' '
        else:
            if len(element) == 1:
                print("'" + '0' + element +"'")
                line += "'" + '0' + element +"'" + ' '
            else:
               print("'" + element + "'")
               line += "'" + element + "'" + ' '
  except:
    print(element)
    line += element + ' '

print(line)
