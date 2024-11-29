c,m,n=map(int,input().split())
water=[]
def op1(water,p):
    index=-1
    for i in range(len(water)):
        if water[i][0] == p:
            water[i][1] += 1
            if water[i][1]>=5:
                index=i
            break
    while index!=-1:
        a=index
        b=index
        if len(water)!=1:
            if index==0:
                water[index+1][1]+=1
                if water[index+1][1]>=5:
                    a=index+1
            elif index==len(water)-1:
                water[index-1][1]+=1
                if water[index-1][1]>=5:
                    b=index-1
            else:
                water[index+1][1]+=1
                water[index-1][1]+=1
                if water[index-1][1]>=5:
                    b=index-1
                elif water[index+1][1]>=5:
                    a=index+1

        water.remove(water[index])
        if b!=index:
            index=b
        elif a!=index:
            index=index
        else:
            index=-1




for i in range(m):
    x,w=map(int,input().split())
    water.append([x,w])
water.sort()
for i in range(n):
    p=int(input())
    op1(water,p)
    print(len(water))