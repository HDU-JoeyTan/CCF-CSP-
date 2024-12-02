def check(cabin1,cabin2,m):
    for i in range(m):
        if cabin1[i]<=cabin2[i]:
            return False
    return True

n,m=map(int,input().split())
cabin=[]
for i in range(n):
    cabin.append(list(map(int,input().split())))
for i in range(n):
    up=0
    for j in range(n):
        if j!=i:
            if check(cabin[j],cabin[i],m):
                up=j+1
                break
    print(up)