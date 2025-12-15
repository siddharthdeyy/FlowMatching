t = int(input())
a = []
for i in range(t):
    n = input().split()
    len1 = int(n[0])
    len2 = int(n[1])
    str1 = input()
    str2 = input()
    count = 0
    if(str2 in str1):
        a.append(0)
    else:
        while(count<=5):
            str1 = str1*2
            len1 = len(str1)
            count+=1
            if str2 in str1:
                a.append(count)
                break
            print(str1)
            print(str2)

    if str2 not in str1:
        a.append(-1)
    
for i in range(t):
    print(a[i])