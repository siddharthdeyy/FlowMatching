t = int(input())
a = []
for i in range(t):
    n = int(input())
    if (n%3==0):
        a.append('Second')
    else:
        a.append('First')

for i in range(t):
    print(a[i])
