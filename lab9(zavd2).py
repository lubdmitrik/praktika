import os
f = open("C:/Users/Andriy/Desktop/task2.txt", "r")
Lines = f.readlines()
f.close()

num_a = 0
num_i = 0
num_i5 = 0

for line in Lines:
    if str(line)[0] == "A" or str(line)[0] == 'a':
        num_a += 1
    for i in range(len(str(line))):
        if str(line)[i] == 'i':
            num_i += 1
    if num_i == 5:
        num_i5 += 1
        num_i = 0
    else:
        num_i = 0
print(num_a)
print(num_i5)
