 import random
list_1 = [random.random() for i in range(10)]
list_2 = []
x = len(list_1)
print(x)
for index, item in enumerate(list_1):
    list_2 += [item, item + index +1]
 print(list_2)
