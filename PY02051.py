n=int(input())
b=[]
for i in range(n):
    b.append(list(map(int,input().split())))
if n==2:
    print(1,b[0][1]-1)
else:
    a=[0]*n
    c=[[0 for _ in range(n)] for _ in range(n)] 
    for j in range(2,n):
        c[j][1]=b[0][j]-b[0][1]
        c[1][j]=b[0][1]-b[0][j]
    for j in range(2,n):
        a[1]=(c[1][j]+b[1][j])//2   
        a[j]=(c[j][1]+b[1][j])//2
    for i in range(len(a)):
        if i==0:
            print(b[0][1]-a[1],end=' ')
        else:
            print(a[i],end=' ')
    print()               