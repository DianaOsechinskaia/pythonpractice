print ('Введите число до которого нужно сгенерировать последовательность:')
n=int(input())

nums_gen = (num for num in range(1, n + 1, 2))

print(*nums_gen, sep=' \n')