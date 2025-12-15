t = int(input())
a = []
for i in range(t):
    n = int(input())
    b = input().split()
    for j in range(len(b)):
        b[j] = int(b[j])
    count = 1
    freq = {}
    for num in b:
        freq[num] = freq.get(num, 0) + 1
    n = len(freq)
    if(n==2):
        l = []
        for j in freq:
            l.append(freq[j])
        if(l[0]-l[1]==1 or l[1] - l[0]==1 or l[0]==l[1]):
            a.append('Yes')
        else:
            a.append('No')
    elif(n==1):
        a.append('Yes')
    else:
        a.append('No')

for i in range(t):
    print(a[i])
