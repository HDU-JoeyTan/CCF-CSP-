n,m=map(int,input().split())
appear=[]
sum1=[0 for i in range(m)]
sum2=[0 for i in range(m)]
for i in range(n):
    appear.append([0 for j in range(m)])
    l=list(map(int,input().split()))
    length=l[0]
    l=l[1:]
    for j in l:
        appear[-1][j-1]+=1
for i in range(n):
    for j in range(m):
        if appear[i][j]!=0:
            sum1[j]+=1
        sum2[j]+=appear[i][j]
for i in range(m):
    print(sum1[i],sum2[i],end=' ')
    print()