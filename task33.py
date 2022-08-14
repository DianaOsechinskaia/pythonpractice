def thesaurus(name):
    res = {}
    for element in name:
        arr = []
        if len(res) != 0:
            if element[0].capitalize() in dict.keys(res):
                for key, value in list(res.items()):
                    if element[0].capitalize() in key:
                        arr = value
                        arr.append(element)
                        del res[key]
                        res[key] = arr
                        break
            else:
                arr.append(element)
                res[element[0].capitalize()] = arr
        else:
            arr.append(element)
            res[element[0].capitalize()] = arr

    for key, value in res.items():
     print("{0}: {1}".format(key,value))


a = ''
names = []
while True:
    print('Напишите имена, которое вы хотите добавить:')
    a = str(input())
    if a != 'exit':
        names.append(a)
    else:
        break

thesaurus(names)