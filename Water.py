t = int(input())
w = []
for i in range(t):
    x = input()
    a = input().split('#')
    p = True
    q = True
    for j in range(len(a)):
        if(len(a[j])==0):
            p = True
        else:
            p = False
            break

    for j in range(len(a)):   
        if(len(a[j])>=3):
            q = True
            break
        else:
            q = False

    if(p):
        w.append(0)
    else:
        if(q):
            w.append(2)
        else:
            sum = 0
            for i in range(len(a)):
                sum+=len(a[i])
            w.append(sum)

for i in range(t):
    print(w[i])