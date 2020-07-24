from codecore import *

arr = []
randomize(arr)
print('Початковий вигляд масиву', arr)
print(sorting(arr))
indexing = int(input('Значення потрібного елементу:'))
indexer(arr, indexing)
poslidov(arr)
lowest(arr)
biggest(arr)
avg(arr)
deletdouble(arr)
