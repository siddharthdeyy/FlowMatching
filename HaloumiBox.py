def IsSorted(a):
    t = True
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            t = False 
            break 
    return t

t = int(input())
for i in range(t): 
    n, k = input().split()
    n = int(n)
    k = int(k)
    a = input().split()
    for i in range(n):
        a[i] = int(a[i])
    if k>1 : 
        print('YES')
    else : 
        if(IsSorted(a)):
            print('YES')
        else : 
            print('NO')