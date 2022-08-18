def generate(num):
  for num in range(1, num + 1, 2):
    yield num


my_gen = generate(15)
print(my_gen)
for i in my_gen:
  print(i)
  