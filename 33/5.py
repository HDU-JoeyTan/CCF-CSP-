n,m=map(int,input().split())
folder=[-1]
folder=folder+list(map(int,input().split()))
data=list(map(int,input().split()))
for i in range(n):
    folder[i]=[folder[i],data[i]]