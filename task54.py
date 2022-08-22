import sys
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
first = 0
second = 0
i = 1
while i < len(src):
  first = src[i-1]
  second = src[i]
  if second > first:
     result.append(second)
  i = i + 1
print(result)

print(sys.getsizeof(result))