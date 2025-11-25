t = int(input())
a = []
for i in range(t):
    n = int(input())
    b = input().split()
    for j in range(len(b)):
        b[j] = int(b[j])
    if (b[0]==1):
        a.append('YES')
    else:
        a.append('NO')

for i in range(t):
    print(a[i])
