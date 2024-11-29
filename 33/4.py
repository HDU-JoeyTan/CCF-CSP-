c,m,n=map(int,input().split())
water=[0 for i in range(c)]
def check(water):
    for i in water:
        if i>=5:
            return True
    return False
def op(water,p):
    water[p]+=1
    while check(water):
        for i in range(len(water)):
            if water[i]>=5:
                for j in range(i-1,-1,-1):
                    if water[j]!=0:
                        water[j]+=1
                        break
                for j in range(i+1,len(water)):
                    if water[j]!=0:
                        water[j]+=1
                        break
                water[i]=0
                break

for i in range(m):
    x,w=map(int,input().split())
    water[x-1]=w
for i in range(n):
    p=int(input())
    op(water,p-1)
    sum=0
    for j in water:
        if j!=0:
            sum+=1
    print(sum)
