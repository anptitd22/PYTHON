n,k=int(input()),0
a=list(map(float,input().split()))
f=[1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if a[j]<a[i]:
            f[i]=max(f[i],f[j]+1)
k=n-max(f)
print(k)