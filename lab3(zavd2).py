import random
n = int(input('n = '))
# a = [[0, 1, 2], [1, 5, 3], [2, 3, 4]]
a = [ [random.randint(-10,10) for j in range(n)] for i in range(n)]
print(a)
k = 0
m = 0
# for i in range(n):
#     row = input().split()
#     for j in range(n):
#         row[j] = int(row[j])
#     a.append(row)

for i in range(1, n):
    for j in range(i):
        if (a[i][j] == a[j][i]):
             k = k+1;
    if k == i:
        m = m+1
if (m == n-1):
    print('YES')
else:
    print('NO')
