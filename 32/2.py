import math


def check(n,k):
    a=2
    sum={}
    result=1
    b=math.sqrt(n)
    while n!=1 and a<=b:
        if n%a==0:
            if a in sum:
                sum[a]+=1
            else:
                sum.update({a:1})
            n/=a
        else:
            a+=1
    for i in sum:
        if sum[i]>=k:
            result*=i**sum[i]
    print(result)


q=int(input())
for i in range(q):
    n,k=map(int,input().split())
    check(n,k)